NEW_USER_TAX_ID = {
  "id": "txi_1JMVBQ2eZvKYlo2CIFwKHMJt",
  "object": "tax_id",
  "country": "DE",
  "created": 123456789,
  "customer": "cus_AJ6mqoWgCYI0wY",
  "livemode": 'false',
  "type": "ch_vat",
  "value": "CHF123456789",
  "verification": {
    "status": "pending",
    "verified_address": 'null',
    "verified_name": 'null'
  }
}

CUSTOMER = {
  "id": "cus_AJ6mqoWgCYI0wY",
  "object": "customer",
  "address": "null",
  "balance": 0,
  "created": 1489793598,
  "currency": "usd",
  "default_source": "card_19yUZO2eZvKYlo2CJty7ZtLt",
  "delinquent": "true",
  "description": "Sample user",
  "discount": "null",
  "email": "norval@example.com",
  "invoice_prefix": "19837A7",
  "invoice_settings": {
    "custom_fields": "null",
    "default_payment_method": "null",
    "footer": "null"
  },
  "livemode": 'false',
  "metadata": '',
  "name": 'null',
  "next_invoice_sequence": 45838,
  "phone": 'null',
  "preferred_locales": '',
  "shipping": '',
  "tax_exempt": "none"
}

SWISS_CUSTOMER = {
  "id": "cus_AJ6mqoWgCYI0wY",
  "object": "customer",
  "address": "null",
  "balance": 0,
  "created": 1489793598,
  "currency": "usd",
  "default_source": "card_19yUZO2eZvKYlo2CJty7ZtLt",
  "delinquent": "true",
  "description": "Sample user",
  "discount": "null",
  "email": "norval@example.com",
  "invoice_prefix": "19837A7",
  "invoice_settings": {
    "custom_fields": "null",
    "default_payment_method": "null",
    "footer": "null"
  },
  "livemode": 'false',
  "metadata": '',
  "name": 'null',
  "next_invoice_sequence": 45838,
  "phone": 'null',
  "preferred_locales": '',
  "shipping": '',
  "tax_exempt": "none"
}

NON_SWISS_CUSTOMER = {
  "id": "cus_AJ6mqoWgCYI0wY",
  "object": "customer",
  "address": "null",
  "balance": 0,
  "created": 1489793598,
  "currency": "usd",
  "default_source": "card_19yUZO2eZvKYlo2CJty7ZtLt",
  "delinquent": "true",
  "description": "Sample user",
  "discount": "null",
  "email": "norval@example.com",
  "invoice_prefix": "19837A7",
  "invoice_settings": {
    "custom_fields": "null",
    "default_payment_method": "null",
    "footer": "null"
  },
  "livemode": 'false',
  "metadata": '',
  "name": 'null',
  "next_invoice_sequence": 45838,
  "phone": 'null',
  "preferred_locales": '',
  "shipping": '',
  "tax_exempt": "exempt"
}
import copy
from functools import wraps


def _make_dummy_response(dummy_response, *args, **kwargs):
    # import logger
    import logging

    logging.warning('Watch out!')

    logging.warning('****USING DUMMY API RESPONSE!!! NOT SAFE FOR PRODUCTION!****')

    logging.warning('Dummy Gateway request: Args: {}; kwArgs: {}'.format(args, kwargs))

    logging.error('Dummy Gateway response: {}'.format(dummy_response))

    return copy.deepcopy(dummy_response)


def use_dummy_response(dummy_response):
    from flask import current_app

    def method_decor(wrapped_method):
        @wraps(wrapped_method)
        def wrapper(*args, **kwargs):
            meth_response = {
                True: lambda *a, **kw: _make_dummy_response(dummy_response, *a, **kw),
                False: wrapped_method,
            }[current_app.config['USE_DUMMY_GATEWAY_RESPONSES']](*args,
                                                                 **kwargs)

            return meth_response

        return wrapper

    return method_decor