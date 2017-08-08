from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database import Base, Category, Item

#LOGIN IMPORTS
from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import os
import sys
import logging
#logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

app = Flask(__name__)


#print(os.path.dirname(os.path.abspath(__file__)))


newpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'client_secrets.json')

CLIENT_ID = json.loads(open(newpath, 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog app"

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/catalog/")
def showCatalog():  
    print("Inside showCatalog")
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(desc(Item.id)).limit(10)
    if 'username' in login_session:
        return render_template('catalog.html', categories=categories, items=items, username=login_session['username'])
    else:
        return render_template('catalog.html', categories=categories, items=items, username=None)
    #    print('not in login sesssion')
    #    return render_template('catalogPublic.html', categories=categories, items=items)
    #else:
    #print(login_session['username'])
    #return render_template('catalog.html', categories=categories, items=items, username=login_session['username'])

@app.route("/catalog/<string:cat_name>/items")
def showCategory(cat_name):
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=cat_name).one()
    items = session.query(Item).filter_by(category_id=category.id)

    return render_template('category.html', categories=categories, category=category, items=items)



@app.route("/catalog/<string:category_name>/<string:item_name>")
def showItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    #items = session.query(Item).filter_by(category_id=category.id)
    if 'username' in login_session:
        return render_template('item.html', category=category, item=item, username=login_session['username'])
    else:
        return render_template('item.html', category=category, item=item, username=None)
    

@app.route("/catalog/<string:category_name>/<string:item_name>/edit", methods=['GET', 'POST'])
def editItem(category_name, item_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).order_by(asc(Category.name))
    item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['category']:
            item.category_name = request.form['category']
        return redirect(url_for('showItem', category_name=category_name, item_name=item_name))
    else:
        return render_template('editItem.html', categories=categories, item=item, category=category) 
@app.route("/catalog/<string:category_name>/<string:item_name>/delete", methods=['GET', 'POST'])
def deleteItem(category_name, item_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()

    item = session.query(Item).filter_by(name=item_name).one()

    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showCategory', cat_name=category_name))
    else:
        return render_template('deleteItem.html', item=item, category=category)      

@app.route("/catalog/new", methods=['GET', 'POST'])
def newItem():
    if 'username' not in login_session:
        print('Get Lost')
        return redirect('/login')
    categories = session.query(Category).order_by(asc(Category.name))
    if request.method == 'POST':
        requestName = request.form['category_name'];
        print(requestName)
        requestId = session.query(Category).filter_by(name=requestName).one()
        print(requestId.id)
        newItem = Item(name=request.form['name'], description=request.form['description'], category_id = requestId.id)

        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return  render_template('newItem.html', categories=categories)
#@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',methods=['GET', 'POST'])
@app.route('/login/')
def showLogin():
        state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
        login_session['state'] = state
        return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization connected
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets(newpath, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    print('URL', url)
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route("/catalog.json")
def catalogJSON():
    categories = session.query(Category).order_by(asc(Category.name))
    output = ""
    for category in categories:
        items = session.query(Item).filter_by(category_id=category.id)
        output.append(jsonify(ContentItem = [i.serialize for i in items]))
    return output
if __name__ == '__main__':
    app.debug = True  
    #LOG_FILENAME = 'errors.log'
  
    #logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)  
    app.secret_key = 'super_secret_key'
            
    '''
    <!---->
    <a href = "{{url_for('showItem', category_name=category.name, item_name=i.name)}}">
    clientid: 168375451406-7it9b3k4viqihdt9e8g7ttjvlhfprl8i.apps.googleusercontent.com
    clientsecretion: o1OtQeytTdDD4WA6UmWY-_YD
    '''    


    app.run(host='0.0.0.0', port=8000)