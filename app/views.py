from urllib import urlencode
from flask import url_for, render_template, request

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
    return render_template("login.html", url=url)
    
@app.route("/auth")
def auth():
    try:
        code = request.args['code']
        state = request.args['state']
    except KeyError:
        return "FAIL"

    error = request.args.get('error', False)

    if error:
        return error

    return code + " " + state
