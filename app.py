from re import I
from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import databse, connect_to_database, Pet
from forms import AddForm, EditForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_to_database(app)
databse.create_all()

toolbar = DebugToolbarExtension(app)

@app.route("/")
def list():
    pets = Pet.query.all()
    return render_template("list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_data = Pet(**data)
        databse.session.add(new_data)
        databse.session.commit()
        flash(f"{new_data.name} has been added to database.")
        return redirecr(url_for('list'))
    else:
        return render_template("addfrm.html", form=form)

@app.route("/<int:pet_id", methods=["GET", "POST"])
def edit(pet_id):
    pt = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pt)
    
    if form.validate_on_submit():
        pt.notes = form.notes.data
        pt.availability = form.availability.data
        pt.photo = form.photo.data
        databse.session.commit()
        flash(f"{pt.name} has been updated")
        return redirect(url_for('list'))
    else:
        return render_template("edit.html", form=form, pet=pt)

@app.route("/api/pets/<int:pet_id>", methods=["GET"])
def retrieve_pet_api(pet_id):
    pt = Pet.query.get_or_404(pet_id)
    info = {"name": pt.name, "age": pt.age}
    return jsonify(info)