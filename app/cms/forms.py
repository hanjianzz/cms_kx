from flsk_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
#注册表
class RegisterForm(FlaskForm):
    username = StringField(label=u'用户名', validators=[DataRequired(),Length(1,64)])
    age = StringField(label=u'年龄', validators=[DataRequired(),Length(1,64)])
    sex = StringField(label=u'性别', validators=[DataRequired(),Length(1,64)])
    submit = SubmitField(label=u'马上注册'）
