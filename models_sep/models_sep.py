#encoding:utf-8

from flask import Flask
from models import Article
from exts import  db
import  config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
