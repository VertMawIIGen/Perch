from flask import Flask

app = Flask(__name__)


@app.route("/")    #home page / first thing the user sees
def hello_world():
    return 'Hello World!'

@app.route("/timetable") #the timetable section once you log in
def hello_world():
    return 'Hello World!'

@app.route("/notices") #placeholder for future development
def hello_world():
    return None



if __name__ == '__main__':
    app.run()
