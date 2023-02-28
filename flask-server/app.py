from flask import Flask
from tinydb import TinyDB, Query

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    db = TinyDB('db.json')
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
