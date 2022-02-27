from flask import Blueprint, jsonify, render_template, current_app
from core.service.interface import MessageProtocol


about_bp = Blueprint('about', __name__,
                     url_prefix='/about',
                     template_folder="templates",
                     static_folder="static",)

@about_bp.route('/')
def index():
    return render_template("about.html")

