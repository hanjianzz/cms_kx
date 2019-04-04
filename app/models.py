# encoding:utf-8
from app import db
from datetime import datetime
# 加密函数, generate_password_hash哈希,check_password_hash检测密码是否一致
from werkzeug.security import  generate_password_hash,check_password_hash

# 创建cms用户数据库模型
class CMSUser(db.Model):
    # 设置表名
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<CMSUser %r>' % self.username

    # getter/setter
    # 可以将一个方法定义成属性
    #@property
    #def password(self):
    #    return self._password

    # 重新定义设置方法
    #@password.setter
    #def password(self,raw_password):
        # 加密
    #    self._password = generate_password_hash(raw_password)

    #def check_password(self,raw_password):
        # 原始密码和加密后的密码是否一致
    #    result = check_password_hash(self._password,raw_password)
    #    return result

# 登录会员
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)
    age = db.Column(db.String(3))
    sex = db.Column(db.Integer)
    address = db.Column(db.String(200))
    fellowship = db.Column(db.Integer)
    serve = db.Column(db.Integer)
    userlogin = db.Column(db.Integer)
    remarks = db.Column(db.String(400))
    join_time = db.Column(db.DateTime,default=datetime.now)

    def __init__(self,username,age,sex,address,fellowship,serve,userlogin,remarks):
        self.username = username
        self.age = age
        self.sex = sex
        self.address = address
        self.fellowship = fellowship
        self.serve = serve
        self.userlogin = userlogin
        self.remarks = remarks


    def __repr__(self):
        return '<CMSUser %r>' % self.username

# 侍奉名称
class Serve(db.Model):
    __tablename__ = 'serve'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)

    def __init__(self,name):
        self.name = name

# 部署名称
class Fellowshiperve(db.Model):
    __tablename__ = 'fellowship'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)

    def __init__(self,name):
        self.name = name

# 会员登录信息
class Userlogin(db.Model):
    __tablename__ = 'userlogin'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)

    def __init__(self,name):
        self.name = name