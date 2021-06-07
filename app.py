"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash
from models import db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)
db.create_all()