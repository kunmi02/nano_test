import requests
import math
from flask import current_app

import stripe
from .dummy_response import use_dummy_response, NEW_USER_TAX_ID, CUSTOMER, SWISS_CUSTOMER

def get_vat_value(amount):
  return math.floor((7.7 / 100) * amount)

@use_dummy_response(NEW_USER_TAX_ID)
def create_customer_vat(customer_id, amout):

  stripe.api_key = current_app.config['STRIPE_API_KEY']
  response = stripe.Customer.create_tax_id(
  customer_id,
  type="ch_vat",
  value=get_vat_value(amout)
)
  
  return response

@use_dummy_response(CUSTOMER)
def get_customer(customer_id):
  stripe.api_key = current_app.config['STRIPE_API_KEY']
  response = stripe.Customer.retrieve(customer_id)
  
  return response

@use_dummy_response(SWISS_CUSTOMER)
def update_customer_status(customer_id, tax_exempt_status):
  stripe.api_key = current_app.config['STRIPE_API_KEY']
  
  response = stripe.Customer.modify(customer_id, tax_exempt=tax_exempt_status) 
  return response
