from crypt import methods
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class SignUpForm(FlaskForm):

    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password=StringField('Password', validators=[InputRequired()])
    password2=StringField('Confirm Password ', validators=[InputRequired()])
    submit = SubmitField('Submit')

class LogInForm(FlaskForm):
     email = StringField('Email', validators=[InputRequired()])
     password=StringField('Password', validators=[InputRequired()])
     submit = SubmitField('Submit')
