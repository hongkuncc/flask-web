#encoding:utf-8
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)

class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)

db.create_all()

@app.route('/')
def index():
    #增
    # article1=Article(title='aaa',content='bbb')
    # db.session.add(article1)
    # db.session.commit()
    #查
    #select*from article where title='aaa';
    # article1=Article.query.filter(Article.title=='aaa')
    # print 'title:%s'%article1.title
    # print 'content:%s'%article1.content


    # #改
    # #1.先查找需要改的数据
    # article1 = Article.query.filter(Article.title == 'aaa'）
    # #2.修改
    # article1.title='new title'
    # #3.做事务提交
    # db.session.commit()

    # #删
    # #1.查找需要删除的数据
    # article1 = Article.query.filter(Article.title == 'aaa'）
    # #2.删除
    # article1.session.delete(article1)
    # #3.提交
    # db.session.commit()
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)

