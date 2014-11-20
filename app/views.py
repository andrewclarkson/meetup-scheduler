from urllib import urlencode
from flask import url_for

from app import app


@app.route("/")
def index():
    return "Hello!"

@app.route("/login")
def login():
    params = urlencode({
        "response_type": "code",
        "client_id": app.config['CONSUMER_KEY'],
        "redirect_uri": url_for('auth', _external=True)
    })

    url = app.config['AUTHORIZE_URL'] + "?" + params
    return url
    
@app.route("/auth")
def auth():
    return "None"
