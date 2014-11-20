import os

DEBUG = True
AUTHORIZE_URL = 'https://secure.meetup.com/oauth2/authorize'

SERVER_NAME = os.environ['HTTP_HOST']

DEVELOPMENT = os.environ['SERVER_SOFTWARE'].startswith("Development")
PRODUCTION = not DEVELOPMENT
CONSUMER_KEY = 'k3qsdfp3v7sq6j1job03jajsl1'

if PRODUCTION:
    from app.secret import *
else:
    SECRET_KEY = 'Super Secret Key'
