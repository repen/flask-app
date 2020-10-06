from flask import Blueprint, render_template
module02 = Blueprint('module02', __name__)

@module02.route("/module2")
def module02_home(): 
    return render_template("module02/index.html")