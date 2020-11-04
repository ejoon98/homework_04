from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dborder  # 'dbsparta'라는 이름의 db를 만듭니다.있으면 갖고오고 없으면 만들고! 그래서 오타를 주의해야해.


@app.route('/')
def home():
    return render_template('week4_homework.html')


@app.route('/order', methods=['POST'])
def write_order():
    name = request.form["name"]
    count = request.form["count"]
    address = request.form["address"]
    number = request.form["number"]

    db.orders.insert_one({
        'name': name,
        'count': count,
        'address': address,
        'number': number
    })

    return jsonify({'result': 'success', 'msg': '상품이 주문되었습니다!'})

@app.route('/order', methods=['GET'])
def read_order():
    orders = list(db.orders.find({}, {'_id': False}))

    # list로바꿔줘야

    return jsonify({'result': 'success', 'msg': '주문 기록을 잘 로드하였습니다.', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

