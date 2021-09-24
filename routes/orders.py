from flask_restplus import Resource
from app import api
from app import app
from resource.Order import order_payload
from utils import db_utils
from flask import Response
import json



orders_name_space = api.namespace('Orders')
@orders_name_space.route('/')
@api.response(200, 'Success')
@api.response(400, 'Validation Error')
@api.response(500, 'Internal Server Error')


class Order(Resource): 
    def get(self):
        try:
            orders_response = db_utils.filter_last_day_orders()
            app.logger.info('Retrieved {} orders from the last day '.format(len(db_utils.db)))
            return Response(json.dumps(orders_response),  mimetype='application/json')
        except ValueError as e:
            app.logger.info(e)
            return e.args

    @api.expect(order_payload, validate = True)
    def post(self):
        try:
            db_utils.validate_order(api.payload)
            app.logger.info('An order was received called "{}"'.format(api.payload['name']))
            return { "Added {} Successfully".format(api.payload['name'])  }
        except ValueError as e:
            app.logger.info(e)
            return e.args, 400