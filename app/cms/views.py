# encoding:utf-8
from flask import render_template, request, redirect, url_for
from app.models import User
from exts import db
from . import blue


@blue.route('/')
def index():
    return render_template('main/index.html')

@blue.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('main/login.html')
    else:
        username = request.form.get("username", type=str, default=None)
        age = request.form.get("age") 
        sex = request.form.get("sex") 
        youaddress = request.form.get("address")
        fellowship = request.form.get("Fellowship") 
        serve = request.form.get("serve") 
        userlogin = request.form.get("userlogin") 
        remarks = request.form.get("remarks") 
        print(youaddress)
        user= User.query.filter(User.username == username).first()

        if user:
            message="用户名相同请重新输入！"
            return render_template('main/login.html',message=message)
        else:
            user = User(username=username,age=age,sex=sex,address=youaddress,fellowship=fellowship,serve=serve,userlogin=userlogin,remarks=remarks)
            print(user.address)
            db.session.add(user)
            db.session.commit()
            message="注册成功！"
            # 如果注册成功就跳转到login
            return render_template('main/login.html',message=message)


@blue.route('/table')
def table():
    context={
        'users':User.query.all()
    }
    return render_template('main/table.html',**context)


@blue.route('/revise/<id>')
def revise(id):
    context={
        'users':User.query.filter_by(id=id).first()
    }
    return render_template('main/revise.html',**context)

@blue.route('/argue')
def argue():
    return render_template('main/argue.html')

@blue.route('/argue_list')
def argue_list():
    return render_template('main/argue_list.html')

@blue.route('/search_list')
def search_list():
    return render_template('main/search_list.html')