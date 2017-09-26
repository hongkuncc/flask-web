#encoding:utf-8
from flask import Flask,render_template

app =Flask(__name__)


@app.route('/')
def index():
    comments=[
        {
            'user':u'知乎',
            'content':u'xxxxx'
        },
        {
            'user':u'橙子',
            'content':u'XXXX'
        }
    ]
    return render_template('filter.html',comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
