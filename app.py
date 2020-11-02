from flask import Flask
import os
from flask import render_template
from flask import request # 2020/11/02
from flask import redirect
from models import db, Myuser

basedir =os.path.abspath(os.path.dirname(__file__))
                        #print(basedir)

#db파일이 저장되어 있는 경로
dbfile=os.path.join(basedir,"db.sqlite")

app = Flask(__name__)
@app.route('/register',method=['GET','POST'])
def register():
    #return render_template('register.html')
    if request.method=='POST':
        print(request.method)
        userid =request.form.get('userid')
        username=request.form.get('username')
        password=request.form.get('password')
        re_password=request.form.get('re-password')

        if (userid and username and password and re_password) and (password==re_password):
            myuser=Myuser()
            myuser.userid=userid
            myuser.username=userid
            myuser.passworld=password

            db.session.add(myuser)
            db.session.commit()

            return redirect('/')

        return render_template('register.html')


#@app.route('/', method=['GET','POST'])
@app.route('/')
def hello():
    return render_template('hello.html') # rule:templates 폴더에 들어있어야함. ('html파일은 템플릿이라 하는구나~')
                        #print(__name__)
                         #print(app)
if __name__=="__main__":
    print('hello')
    basedir =os.path.abspath(os.path.dirname(__file__))
    print('basedir:{}'.format(basedir))
    dbfile = os.path.join(basedir,'db.sqlite')

    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #DATA 업데이트 바로해준다. 누군가 웹페이지 정보요청 했을 때 바로 커밋
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  #SQLAlchemy로 데이터베이스를 여는 것이다.
    db.app = app
    db.create_all()
    app.run(host='127.0.0.1', port=5001, debug=True) #다시 실행하면 port가 겹쳐서 실행안되는경우가 있음. -> port 번호 변경
