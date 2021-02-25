# -*- coding: utf-8 -*-
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Local
from scripts.helpers import session_scope, hash_password

SQLALCHEMY_DATABASE_URI = 'sqlite:///accounts.db'

# Heroku
# SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(SQLALCHEMY_DATABASE_URI)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(512))
    email = Column(String(50))

    def __repr__(self):
        return '<User %r>' % self.username

    def get_otp(self):
        hour = str(int((datetime.now().hour + 1.5) * 2.57))
        if hour.__len__() == 1:
            hour = "0" + hour
        minute = str(int(datetime.now().minute / 5))
        if minute.__len__() == 1:
            minute = "0" + minute
        otp = hour + minute + str(int(int(minute) * 8.6))
        print(otp)
        return otp


engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
with session_scope() as s:
    if not s.query(User).all():
        u = User(id=1, username="admin", password=hash_password("admin").decode('utf8'), email="root@localhost")
        s.add(u)
        s.commit()

