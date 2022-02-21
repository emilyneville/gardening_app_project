"""Models for garden planner app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    zone = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    last_modified_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} created={self.created_date}>"


class Plant(db.Model):
    """A plant."""

    __tablename__ = "plants"

    plant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text)

    plant_type = db.Column(db.Text)
    category = db.Column(db.Text)
    sub_category = db.Column(db.Text)
    
    image_url = db.Column(db.Text)
    short_descr = db.Column(db.Text)
    botanical_name = db.Column(db.Text)
    seed_type = db.Column(db.Text)
    fruit_color = db.Column(db.Text)
    breed = db.Column(db.Text)
    maturity = db.Column(db.Text)
    sun = db.Column(db.Text)

    life_cycle = db.Column(db.Text)
    sow_method = db.Column(db.Text)
    fruit_weight_oz = db.Column(db.Text)
    days_to_maturity = db.Column(db.Text)
    row_spacing_in = db.Column(db.Text)
    sow_depth_in = db.Column(db.Text)
    plant_spacing_in = db.Column(db.Text)
    before_planting = db.Column(db.Text)
    planting = db.Column(db.Text)
    watering = db.Column(db.Text)
    days_to_maturity_text = db.Column(db.Text)
    harvesting = db.Column(db.Text)
    tips = db.Column(db.Text)

    plant_weight_in = db.Column(db.Text)
    plant_depth_in = db.Column(db.Text)
    plant_height_in = db.Column(db.Text)
    plant_width_in = db.Column(db.Text)
    zone_list = db.Column(db.Text)

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
        return f"<Favorite favorite_plant_id={self.favorite_plant_id} plant_id={self.plant_id} user_id={self.user}  >"

class Zone(db.Model):
    """A List of possible zones"""

    __tablename__ = "zones"

    zone_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    zone =  db.Column(db.Integer)
    created_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Zone zone_id={self.zone_id}>"

class PlantZone(db.Model):
    """A List of possible zones"""

    __tablename__ = "plant_zones"

    plant_zone_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.plant_id"), nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey("zones.zone_id"), nullable=False)
    created_date = db.Column(db.DateTime)

    plant = db.relationship("Plant", backref="plant_zones")
    zone = db.relationship("Zone", backref="plant_zones")

    def __repr__(self):
        return f"<PlantZone plant_zone_id={self.plant_zone_id}>"

class UserGantt(db.Model):
    """Gantt chart data a user has made."""

    __tablename__ = "user_gantts"

    user_gantt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    gantt_name = db.Column(db.Text)
    created_date = db.Column(db.DateTime)
    last_modified_date = db.Column(db.DateTime)

    user = db.relationship("User", backref="user_gantts")

    def __repr__(self):
        return f"<UserGantt user_gantt_id={self.user_gantt_id} gantt_name= {self.gantt_name}>"

class UserGanttPlant(db.Model):
    """Plant Items for a User Gantt Chart"""

    __tablename__ = "user_gantt_plants"

    user_gantt_plant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plant_id = db.Column(db.Integer, db.ForeignKey("plants.plant_id"))
    user_gantt_id = db.Column(db.Integer, db.ForeignKey("user_gantts.user_gantt_id"))
    display_name = db.Column(db.Text)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_date = db.Column(db.DateTime)
    last_modified_date = db.Column(db.DateTime)

    plant = db.relationship("Plant", backref="user_gantt_plants")
    user_gantt = db.relationship("UserGantt", backref="user_gantt_plants")

    def __repr__(self):
        return f"<Favorite favorite_plant_id={self.favorite_plant_id}>"


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