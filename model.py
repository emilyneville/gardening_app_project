"""Models for garden planner app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    zone = db.Column(db.String)
    created_date = db.Column(db.DateTime)
    last_modified_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} created={self.created_date}>"


class Plant(db.Model):
    """A plant."""

    __tablename__ = "plants"

    plant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.Text)
    image_url = db.Column(db.Text)
    # dim1 = db.Column(db.String)
    # dim2 = db.Column(db.String)
    created_date = db.Column(db.DateTime)
    last_modified_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Plant plant_id={self.plant_id} name={self.name}>"

class PlantFavorite(db.Model):
    """A user."""

    __tablename__ = "plant_favorites"

    favorite_plant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.plant_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    created_date = db.Column(db.DateTime)


    plant = db.relationship("Plant", backref="plant_favorites")
    user = db.relationship("User", backref="plant_favorites")

    def __repr__(self):
        return f"<Favorite favorite_plant_id={self.favorite_plant_id}>"


class PlantZone(db.Model):
    """A zone for a plant."""

    __tablename__ = "zones"

    zone_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.plant_id"))
    created_date = db.Column(db.DateTime)


    plant = db.relationship("Plant", backref="zones")

    def __repr__(self):
        return f"<Zone zone_id={self.zone_id}>"


def connect_to_db(flask_app, db_uri="postgresql:///plants", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)