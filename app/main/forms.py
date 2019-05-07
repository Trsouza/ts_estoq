from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Usuario

