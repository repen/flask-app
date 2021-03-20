import os
from flask import Flask
from config   import BASE_DIR, PRODUCTION_WORK
from datetime import datetime


def create_app():

    app = Flask(__name__)
    app.secret_key = os.urandom(24)

    from f_api.views  import Api
    from f_site.views import fsite

    app.register_blueprint( Api )
    app.register_blueprint( fsite )

    @app.route('/')
    def index():
        the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
        return "<h1>Welcome! This Application Flask</h1> <p> It is currently {} </p>".format( the_time )

    @app.errorhandler(404)
    def error_404(error):
        return "404 Not found", 404

    return app

def app_run(app):
    from waitress import serve
    if PRODUCTION_WORK:
        serve(app, host='0.0.0.0', port=5000)
    else:
        app.run(port=5000, host='0.0.0.0', debug=True)

if __name__ == '__main__':
    Application = create_app()
    app_run( Application )