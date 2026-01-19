from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()


class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods.bakery',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    baked_goods = db.relationship('BakedGood', backref='bakery')


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    serialize_rules = ('-bakery.baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
