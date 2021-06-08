"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)

# to serialize the cupcakes 
# all_cupcakes = [Cupcake.query.all()]
# return jsonify

@app.route('/api/cupcakes')
def home_page():

    cupcakes = Cupcake.query.all()
    return render_template('home.html', cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_info():
    return "cupcake"

@app.route('/test')
def test_json():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)