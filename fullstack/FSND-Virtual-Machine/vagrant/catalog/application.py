from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from database import Base, Category, Item

# LOGIN IMPORTS
from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from functools import wraps
import httplib2
import json
from flask import make_response
import requests
import os
import sys
import logging
# logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

app = Flask(__name__)


# print(os.path.dirname(os.path.abspath(__file__)))


newpath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'client_secrets.json')

CLIENT_ID = json.loads(open(newpath, 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog app"

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@app.route("/catalog/")
def showCatalog():
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(desc(Item.id)).limit(10)
    if 'username' in login_session:
        return render_template(
            'catalog.html',
            categories=categories,
            items=items,
            username=login_session['username']
            )
    else:
        return render_template(
            'catalog.html',
            categories=categories,
            items=items,
            username=None
            )


@app.route("/catalog/<string:cat_name>/items")
def showCategory(cat_name):
    """
    Show category and items of category
    Keyword arguments:
    cat_name -- name of the category
    Returns:
        A render_template of the category page
    """
    categories = session.query(Category).order_by(asc(Category.name))
    category = session.query(Category).filter_by(name=cat_name).one()
    items = session.query(Item).filter_by(category_id=category.id)
    item_count = items.count()
    print(item_count)
    return render_template(
        'category.html',
        categories=categories,
        category=category,
        items=items,
        item_count=item_count
        )


@app.route("/catalog/<string:category_name>/<string:item_name>")
def showItem(category_name, item_name):
    """
    Show item name and description
    Keyword arguments:
    category_name -- Name of the catgory of the item to be deleted.
    item_name -- Name of item to be deleted.
    Returns:
        A render_template for item page with and without edit and delete
    """
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    # items = session.query(Item).filter_by(category_id=category.id)

    print("Inside showItem", category_name, item_name)

    if 'username' in login_session:
        return render_template(
            'item.html',
            category=category,
            item=item,
            username=login_session['username']
            )
    else:
        return render_template(
            'item.html',
            category=category,
            item=item,
            username=None)


@app.route(
    "/catalog/<string:category_name>/<string:item_name>/edit",
    methods=['GET', 'POST'])
@login_required
def editItem(category_name, item_name):
    """
    Edit item page.
    Keyword arguments:
    category_name -- Name of the catgory of the item to be deleted.
    item_name -- Name of item to be deleted.
    Returns:
        if not logged in redirects to login page
       A redirect to category when edited.
       A render template for the edit item page.
    """
    #if 'username' not in login_session:
    #    return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).order_by(asc(Category.name))
    item = session.query(Item).filter_by(name=item_name).one()

    if item.category_id != login_session['username']:
        flash('You cannot edit %s' % item.name)
        return redirect(url_for(
            'showItem',
            category_name=category_name, item_name=item_name))

    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form['category']:
            item.category_name = request.form['category']
        return redirect(url_for(
            'showItem',
            category_name=category_name, item_name=item_name))
    else:
        return render_template(
            'editItem.html',
            categories=categories,
            item=item, category=category)


@app.route(
    "/catalog/<string:category_name>/<string:item_name>/delete",
    methods=['GET', 'POST'])
@login_required
def deleteItem(category_name, item_name):
    """
    Delete Item page
    Keyword arguments:
    category_name -- Name of the catgory of the item to be deleted.
    item_name -- Name of item to be deleted.
    Returns:
       if not logged in redirects to login page
       A redirect to category when deleted.
       A render template for the delete item page.
    """
    #if 'username' not in login_session:
    #    return redirect('/login')
    category = session.query(Category).filter_by(name=category_name).one()

    item = session.query(Item).filter_by(name=item_name).one()

    if item.category_id != login_session['username']:
        flash('You cannot delete %s' % item.name)
        return redirect(url_for(
            'showItem',
            category_name=category_name, item_name=item_name))


    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showCategory', cat_name=category_name))
    else:
        return render_template('deleteItem.html', item=item, category=category)


@app.route("/catalog/new", methods=['GET', 'POST'])
@login_required
def newItem():
    """
    Makes a new item in the catalog
    Keyword arguments:
    None
    Returns:
        A redirect to catalog once commited.
        A render_template for new item page.
    """
    #if 'username' not in login_session:
    #    return redirect('/login')
    categories = session.query(Category).order_by(asc(Category.name))
    if request.method == 'POST':
        requestName = request.form['category_name']
        requestId = session.query(Category).filter_by(name=requestName).one()

        newItem = Item(
            name=request.form['name'],
            description=request.form['description'],
            category_id=requestId.id)

        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newItem.html', categories=categories)


@app.route('/login/')
def showLogin():
    """
    Forms state token and displays login page.
    Keyword arguments:
    None
    Returns:
        A render_template of the login page.
    """
    state = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits
            )
        for x in xrange(32)
        )
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """
    Log in the selected user
    Keyword arguments:
    None
    Returns:
        Response containing username and picture.
    """
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
        response = make_response(
            json.dumps('Current user is already connected.'),
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
    output += ' " style = "width: 300px; height: 300px;border-radius:150px;\
    -webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    """
    Logs out the connected user
    Keyword arguments:
    None
    Returns:
        Output containing status of log-out.
    """
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(
            json.dumps('Current user not connected.'), 401)
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
        return redirect(url_for('showCatalog'))
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


@app.route("/catalog.json")
def catalogJSON():
    """
    Creates a json endpoint for catalog.db
    Keyword arguments:
    None
    Returns:
        A response containing JSON serialized output.
    """
    categories = session.query(Category).order_by(asc(Category.name))
    output = {}
    categories_json = {}
    for category in categories:
        cat_json = {}
        cat_json['id'] = str(category.id)
        cat_json['name'] = category.name
        cat_json['Item'] = {}
        items = session.query(Item).filter_by(category_id=category.id).all()
        items_json = {}
        for item in items:
            item_json = {}
            item_json['cat_id'] = category.id
            item_json['description'] = item.description
            item_json['id'] = item.id
            items_json[str(item.id)] = item_json

        cat_json['Item'] = items_json
        # output['Activity']['Subactivity']['subsubactivity'] = value
        output[str(category.id)] = cat_json

    categories_json['Category'] = output

    print(categories_json)
    return jsonify(**categories_json)


if __name__ == '__main__':
    app.debug = True

    app.secret_key = 'super_secret_key'

    '''
    clientsecretion: bV5cGrBOuYoE1DV8zpxTmANB
    '''
    app.run(host='0.0.0.0', port=8000)
