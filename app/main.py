import os
import argparse

def create_app(flask_config="default"):
    from flask import Flask
    from config import config
    from database import AppDatabase
    from core.routing import blueprint_list

    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    app.config.from_object(config[flask_config])
    config[flask_config].init_app(app)
    AppDatabase.init_app(app)


    routes = [app.register_blueprint(x) for x in blueprint_list]
    return app


def run_develop(app):
    app.run(port=5000, host='0.0.0.0', debug=True)

def run_production(app):
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Running the application.'
    )

    parser.add_argument('-c', '--config', dest='config', type=str, required=True,
                        help='An example:\npython main.py --config development|testing|default')

    args = parser.parse_args()
    Application = create_app(args.config)

    if args.config == "testing" or args.config == "development":
        run_develop(Application)
    else:
        run_production(Application)
