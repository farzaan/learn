from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine, asc
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

'''
newpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'client_secrets.json')

CLIENT_ID = json.loads(open(newpath, 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu"
'''
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
@app.route("/catalog/")
def showCatalog():  
    categories = session.query(Category).order_by(asc(Category.name))
    items = session.query(Item).order_by(asc(Item.id)).limit(10)
    return render_template('catalog.html', categories=categories, items=items)

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

    return render_template('item.html', category=category, item=item)

@app.route("/catalog/<string:category_name>/<string:item_name>/edit", methods=['GET', 'POST'])
def editItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    categories = session.query(Category).order_by(asc(Category.name))
    item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        if request.form['description']:
            item.description = request.form['description']
        if request.form:
            item.category_name = request.form['category']
        return redirect(url_for('showItem', category_name=category_name, item_name=item_name))
    else:
        return render_template('editItem.html', categories=categories, item=item, category=category) 
@app.route("/catalog/<string:category_name>/<string:item_name>/delete", methods=['GET', 'POST'])
def deleteItem(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name=item_name).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        return redirect(url_for('showItem', category_name=category_name, item_name=item_name))
    else:
        return render_template('deleteItem.html', item=item, category=category)      

@app.route("/catalog/new", methods=['GET', 'POST'])
def newItem():
    categories = session.query(Category).order_by(asc(Category.name))
    if request.method == 'POST':
        requestName = request.form['category_name'];
        resqestId = session.query(Category).filter_by(name=requestName)
        newItem = Item(name=request.form['name'], description=request.form['description'], category_id = requestId.name)

        session.add(newItem)
        session.commit()
        return redirect(url_for('showCatalog'))
    else:
        return  render_template('newItem.html', categories=categories)
#@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',methods=['GET', 'POST'])
#def editItem()

if __name__ == '__main__':
    app.debug = True  
    #LOG_FILENAME = 'errors.log'
  
    #logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)  
    app.secret_key = 'super_secret_key'
            
    '''
    <!---->
    <a href = "{{url_for('showItem', category_name=category.name, item_name=i.name)}}">
    clientid: 168375451406-pmikr862nn05e4254vbbs4rhrqa1neft.apps.googleusercontent.com
    clientsecretion: Tbx2_r-RgGrF_0wzQJQLGHNc
    '''    


    app.run(host='0.0.0.0', port=8000)