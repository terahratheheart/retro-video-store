from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # app.config['SQLALCHEMY_ECHO'] = True

    # Import models here for Alembic setup
    from app.models.video import Video
    from app.models.customer import Customer
    from app.models.rental import Rental

    db.init_app(app)
    migrate.init_app(app, db)

    # # Register Blueprints here

    from .routes import customer_bp
    from .routes import video_bp
    from .routes import rental_bp
    
    app.register_blueprint(customer_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(rental_bp)

    return app
