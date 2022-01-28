"""CRUD operations."""

from model import db, User, Plant, PlantFavorite, connect_to_db
from datetime import datetime


## TODO update the create user intake params
def create_user(email, password):
    """Create and return a new user."""

    user = User(
        email=email, 
        password=password, 
        zone="dummy variable", 
        created_date = datetime.now(), 
        last_modified_date = datetime.now()
        )

    return user



if __name__ == "__main__":
    from server import app

    connect_to_db(app)
