from authlib.integrations.flask_client import OAuth
from flask import Flask, url_for, redirect, render_template, session, Response
import requests
from datetime import timedelta
import os

def fetch_data(location: str, params: dict = {}):
    return requests.get((appConfig.get('CANVAS_URL') + location),
                        headers={"Authorization": f"Bearer {os.environ.get('CANVAS_TOKEN')}"},
                        params=params)


def fetch_new_token():
    return oauth.testApp.fetch_access_token(refresh_token=session['token']['refresh_token'],
                                            grant_type='refresh_token')


app = Flask(__name__)
app.jinja_env.globals.update(fetch_new_token=fetch_new_token)

appConfig = {
    "OAUTH2_CLIENT_ID": os.environ.get("OAUTH2_CLIENT_ID"),
    "OAUTH2_CLIENT_SECRET": os.environ.get("OAUTH2_CLIENT_SECRET"),
    "BASE_URL": os.environ.get("BASE_URL"),
    "FLASK_SECRET": os.environ.get("FLASK_SECRET"),
    "FLASK_PORT": os.environ.get("FLASK_PORT")
}


app.secret_key = appConfig.get("FLASK_SECRET")

oauth = OAuth(app)
oauth.register(
    "testApp",
    client_id=appConfig.get("OAUTH2_CLIENT_ID"),
    client_secret=appConfig.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={
        "scope": "all-ro",
        "state": "abc",
    },
    authorize_url=f"{appConfig.get('BASE_URL')}/authorize",
    access_token_url=f"{appConfig.get('BASE_URL')}/token",
)


@app.route("/canvas")
def canvas():
    user_info = requests.get((os.environ.get('CANVAS_URL') + "/api/v1/users/self"),
                 headers={"Authorization": f"Bearer {os.environ.get('CANVAS_TOKEN')}"})
    return render_template("test.html", pretty=user_info)


# "https://student.sbhs.net.au/api/<component>/<method>.<return format>?<parameters>"

# Authorisation Endpoint:	https://student.sbhs.net.au/api/authorize
# Token Endpoint:	https://student.sbhs.net.au/api/token
# API Scopes: all-ro - read-only access to a student's Portal data
# API Resource Endpoint:	https://student.sbhs.net.au/api/
# client_id
# client_secret

if __name__ == '__main__':
    app.run(debug=True)
