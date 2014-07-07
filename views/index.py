# -*- coding: utf-8 -*-

from flask import render_template

from application import app
from views import register_asset

@app.route('/')
def index():
    return render_template('index.html')

register_asset('index.css', 'index.sass')
register_asset('index.js', 'index.coffee')
