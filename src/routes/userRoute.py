from flask import Blueprint, request
from src.controllers.userController import *

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def login():
    return login_controller(request)

@user_bp.route("/signup", methods=["POST"])
def signup():
    return signup_controller(request)


