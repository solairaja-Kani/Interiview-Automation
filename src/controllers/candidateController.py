
import datetime
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.candidateModel import Candidate
from src import db  # Import your Flask app

def create_candidate(req):
    pass