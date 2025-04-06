from flask import Blueprint, request
from src.controllers.candidateController import *

candidate_bp = Blueprint("users", __name__, url_prefix="/users")

@candidate_bp.route("/", methods=["POST"])
def create():
    return create_candidate(request)


