from datetime import datetime

from api.core import db


class Client(db.Model):

    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256))
    country = db.Column(db.String(256))
    vat_number = db.Column(db.String(256))
    client_id = db.Column(db.String(256))
    stripe_customer_id = db.Column(db.String(256))
    added_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    def as_json(self):
        return {
            'name': self.name,
            'client_id': self.client_id,
            'added_at': self.added_at.isoformat(),
            'country': self.country,
            'vat_number': self.vat_number,
            'stripe_customer_id': self.stripe_customer_id
        }
    def get_country(self, country_code):
        return self.country == country_code

