#===============================================================================
# __init__.py
#===============================================================================

"""Initialization

This file contains the application factory for the okscope app.
"""




# Imports ======================================================================

import os
from flask import Flask, render_template, url_for




# Functions ====================================================================

def create_app(test_config=None):
    """The application factory function

    This function creates and configures the Flask application object. For
    more on application factories, see the Flask documentation/tutorial:

    http://flask.pocoo.org/docs/1.0/tutorial/factory/

    http://flask.pocoo.org/docs/1.0/patterns/appfactories/

    Parameters
    ----------
    test_config : dict
        A dictionary containing configuration parameters for use during unit
        testing. If this parameter is `None`, the configuration will be loaded
        from `config.py` in the instance folder.

    Returns
    -------
    Flask
        A flask app
    """

    app = Flask(__name__, instance_relative_config=True)
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def index():
        return render_template('index.html', nav_button="About", url=url_for('about'))
    
    @app.route('/about')
    def about():
        return render_template('about.html', nav_button="Back", url=url_for('index'))
    
    return app
