# encoding:utf-8
from flask import render_template
from . import blue


@blue.route('/')
def index():
    return render_template('main/index.html')