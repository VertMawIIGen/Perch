from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")  # home page / first thing the user sees
def homepage(): #todo: login function
    return render_template("homepage.html")


@app.route("/treetop")  # the timetable section once you log in
def hello_world():
    return 'Hello World!'


@app.route("/nest")  # placeholder for future development probably the daily notices
def hello_world():
    return None


if __name__ == '__main__':
    app.run()
