import os

DEBUG = True
AUTHORIZE_URL = 'https://secure.meetup.com/oauth2/authorize'

SERVER_NAME = os.environ['HTTP_HOST']

DEVELOPMENT = os.environ['SERVER_SOFTWARE'].startswith("Development")
PRODUCTION = !DEVELOPMENT

if PRODUCTION:
    from app.secret import *
else:
    SECRET_KEY = 'Super Secret Key'
