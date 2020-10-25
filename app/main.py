import os
from flask import Flask, render_template

from module01.views import module01
from module02.views import module02
from config   import BASE_DIR, EXTERNAL_WORK
from waitress import serve
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint( module01 )
app.register_blueprint( module02 )

@app.route('/')
def index():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return "<h1>Flask Main</h1> <p> It is currently {} </p>".format( the_time )

@app.errorhandler(404)
def error_404(error):
    return "404 Not found", 404
    # return render_template("404.html", error=error, code_error = 404), 404



def app_run():
    if EXTERNAL_WORK:
        serve(app, host='0.0.0.0', port=5000)
    else:
        app.run(port=5000, host='0.0.0.0', debug=True)

if __name__ == '__main__':
    app_run()