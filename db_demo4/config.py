#encoding:utf-8


USERNAME = 'root'
PASSWORD ='root'
HOSTNAME ='127.0.0.1'
PORT='3306'
DATABASE='db_demo4'
DB_URI='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
        HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI =DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True