#encoding:utf-8



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)

# #用户表
# create table users(
#     id int primary key autoincrement,
# ____username varchar(100) not null
# )
# #文章表
# create table article(
#     id int primary key autoincrement,
#     title varchar(100) not null,
#     content text not null,
#     author_id_int,
#     foreign key 'author_id'reference 'user.id'
# )

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String(100),nullable=False)
    content=db.Column(db.Text,nullable=False)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id')) #表名

    author=db.relationship('User',backref=db.backref('article'))

db.create_all()
@app.route('/')
def index():
    #想要添加一篇文章，必须先要添加一个用户
    # user1=User(username='chk')
    # db.session.add(user1)
    # db.session.commit()

    # article=Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()

    #找到文章标题为aaa的这个作者
    # article=Article.query.filter(Article.title=='aaa').first()
    # author_id=article.author_id
    # user=User.query.filter(User.id==author_id).first()
    # print'username:%s' % user.username

    # article.author
    # author=User.query.filter(User.username=='chk').first()
    # author.articles

    # article=Article(title='aaa',content='bbb')
    # article.author=User.query.filter(User.id==1).first()
    # db.session.add(article)
    # db.session.commit()

    # #找到标题为aaa的这个作者
    # article = Article.query.filter(Article.title=='aaa').first()
    # print 'username:%s'%article.author.username

    # #找到chk这个用户写过的所有文章
    # article=Article(title='111',content='222',author_id=1)
    # db.session.add(article)
    # ab.session.commit()
    user=User.query.filter(User.username=='chk').first()
    result=user.articles
    for article in result：
        print '-'*10
        print article.title
        

    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
