from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddCupcakeForm(FlaskForm):
    '''Form for adding a new cupcake'''

    flavor = StringField("Cupcake Flavor", validators=[InputRequired()])
    size = StringField("Cupcake Size", validators=[InputRequired()])
    rating = FloatField("Cupcake Rating", validators=[InputRequired()])
    image = StringField("Cupcake Image", validators=[InputRequired(), URL()])

class EditCupcakeForm(FlaskForm):
    '''Edit a cupcake's info'''

    flavor = StringField("Cupcake Flavor", validators=[InputRequired()])
    size = StringField("Cupcake Size", validators=[InputRequired()])
    rating = FloatField("Cupcake Rating", validators=[InputRequired()])
    image = StringField("Cupcake Image", validators=[InputRequired(), URL()])