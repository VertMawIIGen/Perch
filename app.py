from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_file, make_response
from flask_oidc import OpenIDConnect
from config import Config
from flask_wtf.csrf import CSRFProtect
import pprint
import json
import requests
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(Config)

oidc = OpenIDConnect(app)
csrf = CSRFProtect(app)


# Login page redirecting to the school.
@app.route('/login')
@oidc.require_login
def login():
    return redirect(url_for("daily_timetable"))


# landing page / first thing the user sees
@app.route("/")
def landing_page():
    if oidc.user_loggedin:
        flash("Successfully logged in.", "success")
        return redirect(url_for("daily_timetable"))
    else:
        return render_template("landing_page.html")


@app.route("/treetop")  # the timetable section once you log in
@oidc.require_login
def daily_timetable():
    # attempting to get authenticated api information
    # using the requests library
    access_token = session['oidc_auth_token'].get('access_token')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    student_timetable = requests.get('https://student.sbhs.net.au/api/timetable/daytimetable.json', headers=headers)
    student_data = student_timetable.json()

    # pprint.pprint(json_data)

    # list of dictionaries
    daily_bells = student_data.get('bells')
    room_variations = student_data.get('roomVariations')
    teacher_variations = student_data.get('classVariations')
    student_timetable = student_data.get('timetable')

    bell_information = requests.get('https://student.sbhs.net.au/api/timetable/bells.json')
    bell_data = bell_information.json()


   # print(daily_bells)

    return render_template("daily_timetable.html", daily_bells=daily_bells, room_variations=room_variations,
                           teacher_variations=teacher_variations, student_timetable=student_timetable, bell_data = bell_data)


@app.route("/nest")
@oidc.require_login
def daily_notices():
    access_token = session['oidc_auth_token'].get('access_token')
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get('https://student.sbhs.net.au/api/dailynews/list.json', headers=headers)
    json_data = response.json()
    notices = json_data.get('notices')
    return render_template('daily_notices.html', notices=notices)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('landing_page'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
