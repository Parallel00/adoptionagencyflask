from flask_sqlalchemy import SQLAlchemy

databse = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = "pet"
    id = databse.Column(databse.Integer, primary_key=True)
    name = databse.Column(databse.Text, nullable=False)
    animal = databse.Column(databse.Text, nullable=False)
    photo = databse.Column(databse.Text)
    age = databse.Column(databse.Integer)
    notes = databse.Column(databse.Text)
    availability = databse.Column(databse.Boolean, nullable=False, default=True)

    def img(slf):
        return slf.photo

def connect_to_database(app):
    databse.app = app
    databse.init_app(app)