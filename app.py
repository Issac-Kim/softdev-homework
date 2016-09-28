from flask import Flask, render_template
from utils import occupations

app = Flask(__name__)

d = occupations.get_dict()


@app.route("/")
def welcome():
    return "Welcome!"

@app.route("/occupations/")
def webpage():
    job = occupations.random_job()
    return render_template('main.html', keys = d, job = job, percentage = d[job][0], link = d[job][1])
if __name__ == '__main__':
    app.debug = True
    app.run()
