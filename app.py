from flask import Flask, request, render_template, abort, redirect, session
from fake_db import get_all, get_by_id, login as lgn, remove_one, add_by_id
from dotenv import load_dotenv
import requests
import datetime
import logging
import os
from utils import retry
app = Flask(__name__)
app.config['SECRET_KEY'] = "somethingyoudontwannaseeissupposedtobehereLOL"

@retry
def request_method(url, body):
    res = requests.post(url, json=body, timeout=2)
    if res.status_code == 400:
        raise requests.exceptions.HTTPError
    return res.status_code



@app.route('/')
def index():
    items = get_all()
    return render_template('index.html', items=items)



@app.route('/buy/<id>')
def buy(id):
    item = get_by_id(int(id))
    if not item:
        return abort(404, description='Resource not found!')
    
    return render_template("item.html", item=item)
        

@app.route('/buy/<id>', methods=['POST'])
def order(id):
    number = request.form.get('number')
    item = get_by_id(int(id))
    if (not item) or (not number):
        return abort(403)
    if len(number) != 10:
        return "<h3>Invalid Phone Number</h3>"
    body = {
        "item" : item.get("item_name", ""),
        "contact" : number,
        "price" : item.get("price"),
        "time" : str(datetime.datetime.now())
    }

    res = request_method("http://localhost:8000/order", body)

    if res == 0:
        return "<h1>Error Occured.</h1>"

    
    return "<h1>Order Placed</h1>"


@app.route('/admin', methods=['GET'])
def adminPage():
    if "username" not in session:
        return render_template("admin_login.html")
    else:
        items = get_all()
        return render_template("admin_dash.html", items=items)

@app.route('/admin', methods=['POST'])
def login():
    errors = []
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "":
        errors.append("Username cannot be blank.")
    
    if password == "":
        errors.append("Password cannot be blank.")

    if len(errors) != 0:
        return render_template("admin_login.html", errors=errors)
    
    user = lgn(username, password)


    if not user:
        errors.append("Invalid username/password")
        return render_template("admin_login.html", errors=errors)
    else:
        session['username'] = user['username']
        return redirect("/admin")

@app.route('/logout')
def logout():
    del session['username']
    return redirect("/")

@app.route('/delete/<id>')
def deleteItem(id):
    if "username" in session:
        remove_one(int(id))
        return redirect("/admin")
    else:
        return abort(401)

@app.route('/admin/add')
def addItem():
    if "username" in session:
        return render_template("add_item.html")
    else:
        return abort(401)

@app.route('/admin/add' , methods=['POST'])
def addRealItem():
    if "username" not in session:
        return abort(401)
    errors = []

    if 'file' not in request.files:
        errors.append("No files here.")
        return render_template("add_item.html", errors=errors)
    
    file = request.files['file']
    if file.filename == '':
        errors.append("No files here.")
        return render_template("add_item.html", errors=errors)
    
    item = {
        "item_name" : request.form.get("name"),
        "price" : int(request.form.get("price")),
        "image" : file.filename
    }

    add_by_id(**item)
    file.save(os.path.join( os.getcwd(), 'online_shopping_site/static/', file.filename))





if __name__=="__main__":
    app.run()
