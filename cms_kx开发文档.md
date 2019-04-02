cms开发文档
一、项目说明
    1、项目结构
        创建 相关文件:app/
                        __init__.py（蓝图）
                        front/(创建前台)
                        cms/(后台)
                        common/(公共)
                        models.py
                        cms_kx.db
                     config.py
                     exts.py
                     manage.py
    2、项目模型定义
        用户模型models.py
        from exts import db
        from datetime import datetime
        # 加密函数, generate_password_hash哈希,check_password_hash检测密码是否一致
        from werkzeug.security import  generate_password_hash,check_password_hash

        # 创建cms用户数据库模型
        class CMSUser(db.Model):
            # 设置表名
            __tablename__ = 'cms_user'
            id = db.Column(db.Integer,primary_key=True,autoincrement=True)
            username = db.Column(db.String(50),nullable=False)
            _password = db.Column(db.String(100),nullable=False)
            email = db.Column(db.String(50),nullable=False,unique=True)
            join_time = db.Column(db.DateTime,default=datetime.now)

            def __init__(self,username,password,email):
                self.username = username
                self.password = password
                self.email = email

            # getter/setter
            # 可以将一个方法定义成属性
            @property
            def password(self):
                return self._password

            # 重新定义设置方法
            @password.setter
            def password(self,raw_password):
                # 加密
                self._password = generate_password_hash(raw_password)

            def check_password(self,raw_password):
                # 原始密码和加密后的密码是否一致
                result = check_password_hash(self._password,raw_password)
                return result

        # 重写密码字段
        # 密码:对外的字段名叫做password
        #      对内的字段名叫做"_password"

                     