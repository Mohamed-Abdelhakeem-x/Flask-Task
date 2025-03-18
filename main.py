from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def tasks_list():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        completed = 'completed' in request.form
        new_task = Task(title=title, completed=completed)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks_list'))
    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)