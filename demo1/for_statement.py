#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)

#for 遍历字典
@app.route('/')


# def forWord():
#       user={
#           'username':u'橙子',
#             'age':18
#         }
#         websites=['baidu.com','google.com']
#         for k,v in user.items():
#             print k
#             print v
#         return render_template('forWord.html', user=user,websites=websites)


#小案例
def forWord():
    books = [
        {
        'name': u'西游记',
        'author': u'吴承恩',
        'price':100
        },
        {
            'name': u'红楼梦',
            'author': u'吴承恩',
            'price':150
        },
        {
            'name': u'水浒传',
            'author': u'施耐庵',
            'price':130
        },
        {
            'name': u'三国演义',
            'author': u'罗贯中',
            'price':120
        }
    ]
    return render_template('forWord.html',books=books)

if __name__ == '__main__':
    app.run(debug=True)
