from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()],)
    animal = SelectField("Animal", choices[("rabbit", "Rabbit"), ("cat", "Cat"), ("dog", "Dog"), ("fish", "Fish"),],)
    photo = StringField("Photo", validators=[Optional(), URL()],)
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)],)
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)],)

class EditForm(FlaskForm):
    photo = StringField("Photo", validators=[Optional(), URL()],)
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)],)
    availability = BooleanField("Availability")