from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash, send_file, make_response
from flask_oidc import OpenIDConnect
from config import Config
from flask_wtf.csrf import CSRFProtect

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
def daily_timetable():
    return render_template("daily_timetable.html")


@app.route("/nest")  # placeholder for future development probably the daily notices
def something():
    return None


if __name__ == '__main__':
    app.run()
