from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dwqdj 0q09qwd jq0wdj q09jw09j'


@app.route('/', methods=['POST', 'get'])
@app.route("/Add_Task")
def home():
    return render_template("add_task.html", title = "Add Task!", style = "add_task.css")

@app.route("/tasks")
def tasks():
    return render_template("tasks.html", title = "Tasks!", style = "tasks.css")

if __name__ == "__main__":
    app.run(debug=True,port=3000)