from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir =os.path.abspath(os.path.dirname(__file__))
                        #print(basedir)

#db파일이 저장되어 있는 경로
dbfile=os.path.join(basedir,"db.sqlite")

app = Flask(__name__)
                         #print(__name__)
                         #print(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+dbfile
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #DATA 업데이트 바로해준다. WHO 웹페이지 정보요청햇을떄 바로 커밋,
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app) #SQLAlchemy로 데이터베이스를 여는 것이다.

class Test(db.Model):
    __tablename__='test_table'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)

db.create_all()
@app.route('/')
def hello():
    return 'hello world'