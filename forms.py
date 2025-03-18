from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired()])
    completed = BooleanField('Completed')
    submit = SubmitField('Add Task')