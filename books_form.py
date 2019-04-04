from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired


class BooksForm(FlaskForm):
    title = StringField('Ссылка', validators=[DataRequired()])
    content = TextAreaField("Краткое описание", validators=[DataRequired()])
    year = StringField('Год написания', validators=[DataRequired()])
    submit = SubmitField('Добавить')
