from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, Length, regexp
from pkg.password import password_pattern
from marshmallow import Schema, fields

class PasswordLoginReq(FlaskForm):
    """账号密码登陆请求结构"""
    email = StringField('email', validators=[
        DataRequired(),
        Email("登陆邮箱格式错误"),
        Length(min=3, max=254, message="登陆邮箱长度在5~254之间")
    ])
    password = StringField('password', validators=[
        DataRequired("密码不能为空"),
        regexp(regex=password_pattern, message="密码最少包含一个字母,一个数字,并且长度在8~16")
    ])

class PasswordLoginResp(Schema):
    """账号密码授权认证响应结构"""
    access_token = fields.String()
    expire_at = fields.Integer()