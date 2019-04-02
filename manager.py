#coding:utf-8

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from exts import db
# 导入模型
from app import app,models

# 执行命令
# python manage.py db init:初始化
# python manage.py db migrate:执行迁移脚本
# 有可能报AttributeError: 'NoneType' object has no attribute 'encoding'的错误,是因为写数据库连接的时候,utf8写成了utf-8
# python manage.py db upgrade:映射到数据库中


# 初始化app
manager = Manager(app)

# 绑定
Migrate(app,db)
# 映射
manager.add_command('db',MigrateCommand)

# 添加数据
# python manage.py create_cms_user -u miku -p 123456 -e 1479852727@qq.com

if __name__ == "__main__":
    manager.run()
