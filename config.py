#encoding:utf-8
import os
DEBUG=True

SECRET_KEY = os.urandom(24)
DB_URI = "sqlite:///cms_kx.db"

# 数据库
SQLALCHEMY_DATABASE_URI = DB_URI
# 屏蔽SQLalchemy发送的信号
SQLALCHEMY_TRACK_MODIFICATIONS = False