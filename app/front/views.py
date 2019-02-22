# encoding:utf-8
from flask import render_template,views
from . import blue


@blue.route('/')
def index():
    return "这是首页"

# 采用类视图,重写get|post方法

class LoginView(views.MethodView):

    def get(self):
        return render_template('front/index.html')

    def post(self):
        pass