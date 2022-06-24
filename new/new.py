import datetime
import os
from email import message
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

with open('config1.json', 'r') as c:
    params = json.load(c)["params"]
    local_server = params["local_server"]

app = Flask(__name__)

if local_server: \
        app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']

db = SQLAlchemy(app)


class myweb (db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(40), unique=False, nullable=False)
    phone = db.Column(db.String(20), unique=False, nullable=False)
    message = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(30))


@app.route("/home1")
def home1():
    return render_template('home1.html')


@app.route('/man')
def man():
    return render_template('man.html')


@app.route("/women")
def women():
    return render_template("women.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        message = request.form.get('Message')
        entry = myweb(name=name, email=email, phone=phone, message=message, date=datetime.date.today())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html", params=params)

@app.route("/")
def login():
    return render_template("login page.html")


if __name__ == "__main__":
    db.create_all()
    print(os.listdir())
    app.run(debug=True)
