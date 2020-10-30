from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Myuser(db.Model):
    __tablename__ = 'myuser'
    id =db.Column(db.Integer, primary_key=True)
    passworld=db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username=db.Column(db.String(8))