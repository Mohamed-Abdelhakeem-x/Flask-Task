from flask import Flask, render_template, request, redirect, url_for
from forms import TaskForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = '123 456 789'

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/todolist')
def tasks_list():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, completed=form.completed.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks_list'))
    return render_template('add_task.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
