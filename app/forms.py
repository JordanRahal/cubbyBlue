###forms.py
##purpose is to create a login form that users will use to identify with the system
##login is by use of OpenID

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired #DataRequired validator simply checks that the field is not submitted empty

class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)