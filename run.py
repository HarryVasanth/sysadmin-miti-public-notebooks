# -*- coding: utf-8 -*-
"""
    PublicNotebooks

    A simple web interface that list all the Jupyter Netbooks file 
    in the user home directory

    :copyright: (c) 2017 by Mattia Lambertini.
    :license: GPL version 3
"""

from flask import Flask
from flask import render_template, abort, redirect, url_for, request

from os import listdir
from os.path import isfile, join
import re

app = Flask(__name__)
app.config.from_object('config')


def check_username( username ):
    return re.compile(r'[^a-z0-9.]').search(username)

@app.route("/")
def root_page():
    return redirect(url_for('notebook_generic')) 

@app.route("%s/" % app.config['BASE_URL'])
def notebook_generic():
    return render_template('index.html', url=request.url) 

@app.route("%s/<username>" % app.config['BASE_URL'])
def list_notebooks(username):
    # check if the username contains only valid characters
    if check_username(username):
        abort(404)

    mypath = "%s/%s%s" % (app.config['HOME_FOLDER'], username, app.config['NB_FOLDER'])
    try:
        files = tuple(f for f in listdir(mypath) if f.endswith(app.config['NB_EXT']))
    except:
        abort(404)

    return render_template('notebooks.html', username=username, files=files) 

if __name__ == "__main__":
    app.run(host=app.config['IP'], port=app.config['PORT'])
