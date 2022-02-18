"""Server for garden planner app"""

from flask import Flask, render_template, request, flash, session, redirect, url_for
from model import connect_to_db, db, Plant
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

##################################################
#               *** PLANTS ***                   #
##################################################
@app.route("/plants",  methods=["GET"])
def all_plants():
    """View all plants."""

    ##ToDo clean plant category data in sql so this can just be a query on distinct plant categories (rn is messy data)
    plant_category_options = ['Artichoke','Asparagus','Beans','Beets','Broadleaf','Broccoli','Brussel Sprouts','Burdock'
                            ,'Cabbage','Carrot','Cauliflower','Celeriac','Celery','Chard','Chicory','Chinese Cabbage','Collards','Corn','Corn Seed','Cover Crop','Cowpea','Cucumber','Edamame','Eggplant'
                            ,'Fennel','Garlic','Gourd','Green','Horseradish','Jicama','Kale','Kohlrabi','Leek','Lettuce'
                            ,'Melon','Microgreens','Okra','Onion','Parsnip','Pea','Peanuts','Pepper','Potato','Pumpkin'
                            ,'Radish','Rutabaga','Salsify','Shallots','Spinach','Sprouts','Squash','Sweet Potato','Tomatillo'
                            ,'Tomato','Turnips','Watermelon','Zucchini']

    
    keyword = request.args.get("keyword", "")
    category = request.args.get("category", "")

    sun = request.args.get("sun", "")
    color = request.args.get("color", "")

    life_cycle = request.args.get("life-cycle", "")
    category = request.args.get("category", "")
    sub_category = request.args.get("sub_category", "")

    full_search = keyword + sun + color + life_cycle + category + sub_category

    page = request.args.get('page', 1, type=int)

    if full_search.strip() == "":
        ##ToDO verify this isn't excluding any plants (thinking it might be)
        plants = Plant.query.paginate(page=page, per_page=24) 
    
    else:
        ##ToDo make filters apply only when they exist or are not "" 
        plants = Plant.query.filter(
            Plant.name.ilike(f'%{keyword}%'),
            Plant.category.ilike(f'%{category}%'),
            Plant.sun.ilike(f'%{sun}%'),
            Plant.fruit_color.ilike(f'%{color}%'),
            Plant.life_cycle.ilike(f'%{life_cycle}%')
            ).paginate(page=page, per_page=24) 
    
    return render_template("all_plants.html", plants=plants, plant_category_options=plant_category_options,
            keyword=keyword, sun=sun, color=color, life_cycle=life_cycle, category=category, sub_category=sub_category)

@app.route("/plant/<plant_id>")
def show_plant(plant_id):
    """Show details on a particular plant."""
    logged_in_email = session.get("user_email")
    user = crud.get_user_by_email(logged_in_email)
    plant = crud.get_plant_by_id(plant_id)

    if logged_in_email is None:
        current_favorite = False
    elif crud.get_favorite_by_user_and_plant(user.user_id, plant_id) is not None:
        current_favorite = True
    else:
        current_favorite = False
  
    return render_template("plant_details.html", plant=plant, current_favorite=current_favorite)

#################################################
#               *** USERS ***                   #
#################################################

@app.route("/users")
def all_users():
    """View all users."""

    users = crud.get_users()

    return render_template("all_users.html", users=users)

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/user_info", methods=["GET", "POST"])
def show_user():
    """Show details on a particular user."""
    logged_in_email = session.get("user_email")
    user = crud.get_user_by_email(logged_in_email)
    
    if logged_in_email is None:
        flash("You must log in to view profile info.")
        return redirect("/")
    else:
        return render_template("user_details.html", user=user)


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return redirect("/")

#####################################################
#               *** FAVORITES ***                   #
#####################################################

@app.route("/add-favorite", methods=["POST"])
def add_favorite():
    """Add a favorite plant to our database."""
    plant_id = request.json.get("plantId")
    logged_in_email = session.get("user_email")
    plant_id = int(plant_id)
    if logged_in_email is None:
        flash("You must log in to favorite a plant.")
        return { "success": "false"} 
    else:
        user = crud.get_user_by_email(logged_in_email)
        favorite = crud.create_favorite(user.user_id, plant_id)
        db.session.add(favorite)
        db.session.commit()
        return { "success":"true"} 

@app.route("/remove-favorite", methods=["POST"])
def remove_favorite():
    """Remove a favorite plant to our database."""

    plant_id = request.json.get("plantId")
    logged_in_email = session.get("user_email")
    user = crud.get_user_by_email(logged_in_email)
    deleted_favorite = crud.delete_favorite(user.user_id, plant_id)
    db.session.delete(deleted_favorite)
    db.session.commit()
    return { "success": "true"}





##################################################
#               *** GANTTS ***                   #
##################################################

@app.route("/user_gantts")
def all_gantts():
    """Landing page for gantt chart creator / Garden Schedule"""


    return render_template("user_gantts.html")

@app.route("/user_gantt_details")
def gantt_detail():
    """Shows specific gantt chart"""

    return render_template("user_gantt_details.html")

#################################################
#               *** PLOTS ***                   #
#################################################

@app.route("/user_bed_details")
def bed_detail():
    """Shows specific bed design"""

    return render_template("user_bed_details.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
