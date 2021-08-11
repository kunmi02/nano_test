from flask import Blueprint, request
from sqlalchemy.orm.exc import NoResultFound
from api.modules.stripe_api import stripe
from api.core.models import Client
from api.core.utils.response_helpers import (
     make_created_response,
     make_deleted_response,
     make_failure_response,
     make_success_response)

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1.0')

@api_v1.route('/update_tax_id', methods=['GET'])
def add_vat_to_customer_payment():
  customer = request.args.get('customer_id')
  amount = request.args.get('amount')
  response = stripe.create_customer_vat(customer, amount)
  return make_success_response(response)

@api_v1.route('/customer', methods=['GET'])
def retrieve_customer():
  client = request.args.get('client_id')
  country = request.args.get('county_code')
  if country:
    query = Client.query.filter(Client.country == country)
    pagination = query.paginate()
    response_data = [country_client.as_json() for country_client in pagination.items]

    return make_success_response(response_data, meta=pagination.meta)

  return make_failure_response(message = 'Enter customer details', http_code=404)


@api_v1.route('/tax-exempt-status', methods=['GET'])
def add_tax_exempt_to_customer_payment():
  tax_exempt_status = request.args.get('tax_exempt_status')
  country = request.args.get('county_code')
  swiss_client = Client.query.filter(Client.country == country).all()
  for client in swiss_client:
    customer_tax_status = stripe.update_customer_status(client.stripe_customer_id, 'none')
    #captures errors here
  return make_success_response("Customer details has been updated")


