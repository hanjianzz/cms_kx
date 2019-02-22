# encoding:utf-8
from flask import Flask
from exts import db
import config
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# 这是后台用蓝图
from app.cms.views import blue
app.register_blueprint(blue)
# 这是前台用蓝图
from app.front.views import blue
app.register_blueprint(blue)