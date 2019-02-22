from wtforms import Form,StringField,IntegerField
from wtforms.validators import  Email,InputRequired,Length

# 验证登录表单
class LoginForm(Form):
    email = StringField(validators=[Email(message="请输入正确的邮箱格式")])
    password = StringField(validators=[Length(6,20,message="请输入正确格式的密码")])
    remember = IntegerField()