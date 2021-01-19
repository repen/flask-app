from flask import Blueprint, render_template
fsite = Blueprint('fsite', __name__)

@fsite.route("/site")
def main(): 
    return render_template("f_site/index.html")