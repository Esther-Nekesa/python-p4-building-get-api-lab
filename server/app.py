from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    return jsonify([b.to_dict() for b in bakeries]), 200


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get(id)
    if not bakery:
        return jsonify({"error": "Bakery not found"}), 404
    return jsonify(bakery.to_dict()), 200


@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    return jsonify([bg.to_dict() for bg in baked_goods]), 200


@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()

    if not baked_good:
        return jsonify({}), 200

    return jsonify(baked_good.to_dict()), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)
