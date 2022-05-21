from wtforms import Form, DecimalField, IntegerField, TextAreaField, BooleanField, validators, StringField
from wtforms.validators import DataRequired, Length, EqualTo

class Search(Form):
    num = IntegerField("Search For Location", validators=[DataRequired()])
