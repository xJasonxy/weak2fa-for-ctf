# -*- coding: utf-8 -*-

from wtforms import Form, StringField, validators, IntegerField


class LoginForm(Form):
    username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    otp = IntegerField('OTP:', validators=[validators.NumberRange(min=0, max=999999, message='Invalid OTP')])


class SignupForm(Form):
    username = StringField('Username:', validators=[validators.required(), validators.Length(min=1, max=30)])
    password = StringField('Password:', validators=[validators.required(), validators.Length(min=1, max=30)])
    email = StringField('Email:', validators=[validators.Email(), validators.Length(min=0, max=50)])
