#! /usr/bin/env python3
# coding: utf-8
"""
Jean-Pierre [Prototype]
A Raspberry Pi robot helping people to build groceries list.
Matteo Cargnelutti - github.com/matteocargnelutti

controllers/web.py - Web server : uses Flask
"""
#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os

from flask import Flask

from utils import Database
import models

#-----------------------------------------------------------------------------
# Flask WSGI init and routes
#-----------------------------------------------------------------------------
# Database connection
Database.on()

# Flask init
webapp = Flask(__name__)
params = models.Params()

if hasattr(params, 'flask_secret_key'): # If the database is ready
    webapp.config['SECRET_KEY'] = params.flask_secret_key

del params

@webapp.route("/")
def hello():
    return "Hello World!"

# Close database connection
Database.off()

#-----------------------------------------------------------------------------
# Controller
#-----------------------------------------------------------------------------
class Web:
    pass
