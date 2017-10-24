#encoding:utf-8

from flask import Flask,render_template
import  config
from flask import  request
from exts import db
from flask import session
#from models import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        telephone=request.form.get('telephone')
        password=request.form.get('password')
        user=User.query.filter(User.telephone==telephone,User.password==password).first()
        if user:
            session['user_id']=use.id
            #如果在30天内不登录
            session.permanent=True
        else:
            return u'手机号码错误，请确认！'

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        telephone=request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

    user= User.query.filter(User.telephone==telephone).first()
    if user:
        return u'两次密码不相等，请核对后再填写'
    else:
        user=User(User.telephone==telephone,User.password==password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/question/')
def question():
    if request.method=='GET':
        return render_template('question.html')
    else:
        pass

if __name__ == '__main__':
    app.run()
