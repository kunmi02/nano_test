from flask import Flask


def _setup_blueprints(app):
    from api.modules.controllers import stripe

    app.register_blueprint(stripe.api_v1)


def _bind_home_url(app):
    @app.route('/')
    def index():

        return 'Welcome to Azeez Nano Fullstack Software Engineer Solution'


def create_app(configuration_mode):
    from configure import load_configuration

    app = Flask(__name__, instance_relative_config=True)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

    load_configuration(app, configuration_mode)

    _setup_blueprints(app)
    _bind_home_url(app)

    return app

