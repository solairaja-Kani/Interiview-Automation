from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Init db
db = SQLAlchemy()

def create_app():
    # Load env variables
    load_dotenv()

    # Create app
    app = Flask(__name__)
    # Handling CORS
    CORS(app)

    # Config section
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}".format(
            DB_USER=os.getenv("DB_USER"),
            DB_PASSWORD=os.getenv("DB_PASSWORD"),
            DB_HOST=os.getenv("DB_HOST"),
            DB_NAME=os.getenv("DB_NAME"),
        )
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'keepItSecretBczItsASecretKey.12345678909448'


    # Connect the db to app
    db.init_app(app)

    # Init migration
    migrate = Migrate(app, db)

    # Import routes
    # from src.routes.mobile_model_routes import model_bp
    # from src.routes.scheme_routes import scheme_bp
    # from src.routes.model_group_routes import modelgroup_bp
    # from src.routes.price_band_routes import price_band_bp
    # from src.routes.scheme_closure_routes import scheme_closure_bp

    from src.routes.userRoute import user_bp
    
    
    # # mobile model
    # app.register_blueprint(model_bp)
    # # price band
    # app.register_blueprint(price_band_bp)
    # # scheme
    # app.register_blueprint(scheme_bp)
    # # model group
    # app.register_blueprint(modelgroup_bp)
    # # scheme closure
    # app.register_blueprint(scheme_closure_bp)
    app.register_blueprint(user_bp)

    return app
