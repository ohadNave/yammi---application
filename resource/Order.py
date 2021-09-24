from flask_restplus import fields
from app import api


order_payload = api.model('Order', {
    'name': fields.String,
    'price': fields.Float,
    'date': fields.DateTime(dt_format='rfc822'),
})