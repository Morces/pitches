from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired


class PitchForm(FlaskForm):
    pitch = TextAreaField('Enter your pitch')
    name = StringField('Enter your name', validators=[InputRequired()])
    submit = SubmitField('Pitch', validators=[InputRequired()])

