"""CRUD operations."""

from model import db, User, Plant, PlantFavorite, UserGantt, UserGanttPlant, connect_to_db
from datetime import datetime


#################
##### users #####
#################

def create_user(email, password, zone=None):
    """Create and return a new user."""

    user = User(
        email=email, 
        password=password, 
        zone=zone, 
        created_date = datetime.now(), 
        last_modified_date = datetime.now()
        )

    return user

def get_users():
    """Return all users."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


##################
##### plants #####
##################

def create_plant(name, plant_type, category,  image_url, short_descr, botanical_name=None, seed_type=None, fruit_color=None, breed=None,
                maturity=None, sun=None, life_cycle=None, sow_method=None, before_planting=None, planting=None, watering=None, days_to_maturity_text=None,
                harvesting=None, tips=None, sub_category=None, days_to_maturity=None, fruit_weight_oz=None,row_spacing_in=None,
                sow_depth_in=None,plant_spacing_in=None,plant_weight_in=None,plant_depth_in=None,plant_height_in=None,plant_width_in=None,zone_list=None):

    """Create and return a new plant."""
    plant = Plant(
    name=name,
    plant_type=plant_type, 
    category=category,
    sub_category=sub_category,
    image_url=image_url,
    short_descr=short_descr,
    botanical_name=botanical_name,
    seed_type=seed_type,
    fruit_color=fruit_color,
    breed=breed,
    maturity=maturity,
    sun=sun,
    life_cycle=life_cycle,
    sow_method=sow_method,
    before_planting=before_planting,
    planting=planting,
    watering=watering,
    days_to_maturity_text=days_to_maturity_text,
    harvesting=harvesting,
    tips=tips,
    days_to_maturity=days_to_maturity,
    fruit_weight_oz=fruit_weight_oz,
    row_spacing_in=row_spacing_in,
    sow_depth_in=sow_depth_in,
    plant_spacing_in=plant_spacing_in,
    plant_weight_in=plant_weight_in,
    plant_depth_in=plant_depth_in,
    plant_height_in=plant_height_in,
    plant_width_in=plant_width_in,
    zone_list=zone_list,
    created_date=datetime.now(),
    last_modified_date=datetime.now()
    )
    return plant


def get_plants():
    """Return all plants."""

    return Plant.query.all()


def get_plant_by_id(plant_id):
    """Return a plant by primary key."""

    return Plant.query.get(plant_id)


#####################
##### favorites #####
#####################

def create_favorite(user_id, plant_id):
    """Create and return a new favorite plant."""

    favorite = PlantFavorite(user_id=user_id, plant_id=plant_id, created_date=datetime.now())

    return favorite

def delete_favorite(user_id, plant_id):
    """Delete a PlantFavorite with UserID and PlantID."""

    deleted_favorite = PlantFavorite.query.filter_by(user_id=user_id, plant_id=plant_id).first()
    
    return deleted_favorite


def get_favorite_by_user_and_plant(user_id, plant_id):
    """Return a PlantFavorite with UserID and PlantID."""

    return PlantFavorite.query.filter_by(user_id=user_id, plant_id=plant_id).first()

def get_favorites_by_user(user_id):
    """Return a PlantFavorite with UserID and PlantID."""

    return PlantFavorite.query.filter_by(user_id=user_id)



###################
##### gantts ######
###################

def create_user_gantt(user_id, gantt_name):
    """Create and return a new gantt cahart."""
    user_gantt = UserGantt(
    user_id=user_id,
    gantt_name=gantt_name,
    created_date=datetime.now(),
    last_modified_date=datetime.now()
    )
    return user_gantt

def create_user_gantt_plant(user_gantt_id, plant_id, display_name, start_date, end_date):
    """Create and return a new plant as a line in the gantt chart."""
    user_gantt_plant = UserGanttPlant(
    user_gantt_id=user_gantt_id,
    plant_id=plant_id,
    display_name=display_name,
    start_date=start_date,
    end_date=end_date, 
    created_date=datetime.now(),
    last_modified_date=datetime.now()
    )
    return user_gantt_plant

def rebuild_gantt_plants(user_gantt_id, list_of_plants):
    """Add in several plants to a gantt at once"""

    for sub_list in list_of_plants:
        create_user_gantt_plant(user_gantt_id, sub_list[0].plant_id, sub_list[0].name, sub_list[1][0:10], sub_list[2][0:10])
        print(f"attempted to add {sub_list[0].name} to gantt ID {user_gantt_id} ")

    return print('plants have been added!')

def delete_gantt_plants(user_gantt_id):
    """Delete a PlantFavorite with GanttID and PlantID."""

    plants_to_delete = UserGanttPlant.query.filter_by(user_gantt_id=user_gantt_id).all()
    
    return plants_to_delete




def get_gantts_by_user_id(user_id):
    """Return a list of the user's saved Gantt Charts"""
    return UserGantt.query.filter_by(user_id=user_id)

def get_plants_by_gantt_id(user_gantt_id):
    """Return all the Plants associated with a given Gantt Chart"""
    return UserGanttPlant.query.filter_by(user_gantt_id=user_gantt_id)

def get_gantt_by_id(gantt_id):
    return UserGantt.query.get(gantt_id)


def get_gantt_by_name(name):
    return UserGantt.query.filter_by(gantt_name=name).first()


##################
##### zones ######
##################

def create_zone(zone):
    """Create and return a new plant."""
    zone = Zone(
    zone=zone,
    created_date=datetime.now()
    )
    return zone

def create_plant_zone(plant_id, zone_id):
    """Create and return a new plant."""
    plant_zone = PlantZone(
    plant_id=plant_id,
    zone_id=zone_id,
    created_date=datetime.now()
    )
    return plant_zone

if __name__ == "__main__":
    from server import app

    connect_to_db(app)
