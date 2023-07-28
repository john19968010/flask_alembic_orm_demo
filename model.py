from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    gender = Column(Boolean)
    account = Column(String(45))
    password = Column(String(100))
    birth = Column(DateTime)
    note = Column(String(45))
    create_at = Column(DateTime)




