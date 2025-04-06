import jwt
import datetime
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.usersModel import User
from src import db

# Signup Controller
def signup_controller(request):
    data = request.get_json()
    role = data.get("role")
    email = data.get("email")
    password = data.get("password")

    if not role or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter(User.email == email).first():
        return jsonify({"error": "User already exists"}), 409

    hashed_password = generate_password_hash(password)
    user = User(role=role, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# Login Controller with JWT token
def login_controller(request):
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {"username": user.username}
    }), 200
