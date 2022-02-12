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

@app.route("/plants",  methods=["GET"])
def all_plants():
    """View all plants."""
    keyword = request.args.get("keyword", "")
    sun = request.args.get("sun", "")
    color = request.args.get("color", "")
    life_cycle = request.args.get("life-cycle", "")
    category = request.args.get("category", "")
    sub_category = request.args.get("sub_category", "")

    full_search = keyword + sun + color + life_cycle + category + sub_category

    page = request.args.get('page', 1, type=int)

    if full_search.strip() == "":
        plants = Plant.query.paginate(page=page, per_page=24) 
    
    else:
        plants = Plant.query.filter(
            Plant.name.ilike(f'%{keyword}%'),
            Plant.sun.ilike(f'%{sun}%'),
            Plant.fruit_color.ilike(f'%{color}%'),
            Plant.life_cycle.ilike(f'%{life_cycle}%')
            ).paginate(page=page, per_page=24) 
    
    return render_template("all_plants.html", plants=plants)




@app.route("/plant/<plant_id>")
def show_plant(plant_id):
    """Show details on a particular plant."""

    plant = crud.get_plant_by_id(plant_id)

    return render_template("plant_details.html", plant=plant)


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


@app.route("/users/<user_id>")
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

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

@app.route("/user_gantts")
def all_gantts():
    """Landing page for gantt chart creator / Garden Schedule"""


    return render_template("user_gantts.html")

@app.route("/user_gantt_details")
def gantt_detail():
    """Shows specific gantt chart"""


    return render_template("user_gantt_details.html")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
