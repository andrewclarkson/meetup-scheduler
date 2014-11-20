"""
A simple wrapper around the flask app (app/__init__.py)
adds the library directory "lib" into the system path so
that python will recognize any libraries that are put there.
"""

import os
import sys

# add ./lib to the system path
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))

from google.appengine.ext.webapp.util import run_wsgi_app
from app import app

