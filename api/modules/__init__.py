from flask import Flask


def _setup_blueprints(app):
    from answers.modules.controllers import stripe

    app.register_blueprint(stripe.api_v1)


def _bind_home_url(app):
    @app.route('/')
    def index():

        return 'Welcome to Email Subscribers List.'


def create_app(configuration_mode):
    from configure import load_configuration
    from subscription.core import db

    app = Flask(__name__, instance_relative_config=True)

    load_configuration(app, configuration_mode)

    _setup_blueprints(app)
    _bind_home_url(app)

    return app

