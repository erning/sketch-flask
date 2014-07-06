# -*- coding: utf-8 -*-

from flask import render_template

from sketch import app
from sketch.views import register_asset

@app.route('/')
def index():
    return render_template('index.html')

register_asset('index.css', 'common.sass', 'index.sass')
register_asset('index.js', 'index.coffee')
