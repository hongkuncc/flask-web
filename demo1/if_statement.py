#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def ifword(is_login):
    if is_login=='1':
        user={
            'username':u'橙子'
        }
        return render_template('ifword.html', user=user)
    else:
        return render_template('ifword.html')
if __name__ == '__main__':
    app.run(debug=True)
