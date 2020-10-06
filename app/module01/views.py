
from flask import Blueprint, render_template
module01 = Blueprint('module01', __name__)
from models import Car

@module01.route("/module1") 
def module01_home(): 
    return render_template("module01/index.html")


@module01.route("/mfirst") 
def first():
    car = Car()
    return "mfirst " + car.get_car()