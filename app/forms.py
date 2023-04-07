# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])
    poster = FileField("Poster", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Images only!')])
