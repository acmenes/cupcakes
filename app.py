"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)

@app.route('/')
def home_page():
    return render_template('base.html')