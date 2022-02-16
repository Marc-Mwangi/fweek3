from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField 
from wtforms.validators import Email,EqualTo, InputRequired
from ..models import User



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class PitchesForm(FlaskForm):
      pitch = TextAreaField('You have one minute',validators = [InputRequired()])
      submit = SubmitField('Submit')