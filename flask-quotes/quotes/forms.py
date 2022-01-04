from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class QuoteForm(FlaskForm):
    quote = TextAreaField('Quote', validators=[DataRequired()])
    quote_origin = StringField('Quote Origin', validators=[DataRequired()])
    submit = SubmitField('Submit')

