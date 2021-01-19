from flask import Blueprint, jsonify
Api = Blueprint('Api', __name__)


@Api.route("/info") 
def info(): 
    return  jsonify({"error": False, "result": ["hello", "world"] })


@Api.route("/start") 
def start():
    return jsonify({"error": False, "result": ["hello", "world"] })