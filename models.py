"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE_IMG = "https://tinyurl.com/demo-cupcake"

### CLASSES ###

class Cupcake(db.Model):
    '''Cupcake'''

    __tablename__ = "cupcakes"

    id = db.column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.column(db.Text, nullable=False)

    size = db.column(db.Text, nullable=False)

    rating = db.column(db.Float, nullable=False)

    image = db.column(db.Text, nullable=False, default=DEFAULT_CUPCAKE_IMG)

def connect_db(app):
    '''Connect the db to our app'''

    db.app = app
    db.init_app(app)