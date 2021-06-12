from flask import Blueprint, jsonify
from core.service.interface import IBackendProtocol
from datetime import datetime


home_bp = Blueprint('home', __name__)
result01 = IBackendProtocol(message="Successful", data=[1,2,3], status_code=200)
result02 = IBackendProtocol(message="Error", data=[], status_code=403)


@home_bp.route("/data")
def data():
    return  jsonify(result01.to_dict()), result01.status_code


@home_bp.route("/error")
def err_data():
    return jsonify(result02.to_dict()), result02.status_code


@home_bp.route('/')
def index():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return "<h1>Welcome! This Application Flask</h1> <p> It is currently {} </p>".format( the_time )


@home_bp.app_errorhandler(404)
def error_404(error):
    return "<h1>404 Not found</h1>", 404
