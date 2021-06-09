"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, flash, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

from forms import AddCupcakeForm, EditCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'MissMillieIsGood'

connect_db(app)

# to serialize the cupcakes 
# all_cupcakes = [Cupcake.query.all()]
# return jsonify

### BASIC ROUTES###

@app.route('/')
def index_page():
    cupcakes = Cupcake.query.all()
    return render_template ('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def home_page():

    cupcakes = Cupcake.query.all()
    return render_template('home.html', cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def cupcake_info(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return render_template('cupcake.html', cupcake=cupcake)

### ADDING CUPCAKES ###

@app.route('/api/cupcakes/submit', methods =["GET", "POST"])
def add_cupcake():

    form = AddCupcakeForm()

    if form.validate_on_submit():
        new_cupcake = Cupcake(
            flavor = form.flavor.data,
            size = form.size.data,
            rating = form.rating.data,
            image = form.image.data
        )
        db.session.add(new_cupcake)
        db.session.commit()
        return redirect ('/api/cupcakes')

    else:
        return render_template('form.html', form=form)
    
@app.route('/api/cupcakes/submit', methods=["GET"])
def add_cupcake_db():
    new_cupcake = Cupcake()

    db.session.add(new_cupcake)
    db.session.commit()

    return redirect('/api/cupcakes')

### EDITING CUPCAKES ###

@app.route('/api/cupcakes/<int:cupcake_id>/edit', methods=["PATCH"])
def edit_cupcake(cupcake_id):

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    form = EditCupcakeForm()

    if form.validate_on_submit():
        cupcake.flavor = form.flavor.data,
        cupcake.size = form.size.data,
        cupcake.rating = form.rating.data,
        cupcake.image = form.image.data
        db.session.commit()
        return redirect ('/api/cupcakes')
    
    else:
        return "edit"

@app.route('/api/cupcakes/<int:cupcake_id>/delete')
def delete_cupcake():
    return "delete"

### JSON ROUTES ###

@app.route('/json_cupcakes')
def json_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)

@app.route('/json/cupcakes/<int:cupcake_id>')
def single_cupcake_json(cupcake_id):
    serialize_cupcake = [cupcake.serialze() for cupcake in Cupcake.query.get_or_404(cupcake_id)]
    return jsonify(serialize_cupcake)