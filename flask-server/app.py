from flask import Flask, request
from flask_cors import CORS, cross_origin
from tinydb import TinyDB, Query

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = TinyDB('db.json')


@app.route('/', methods=['GET'])
def index():
    return 'Server running...'


@app.route('/add', methods=['POST'])
@cross_origin()
def addItem():
    data = request.get_json()
    db.insert(data)
    # print(request.get_data())
    return ''


if __name__ == '__main__':
    app.run()
