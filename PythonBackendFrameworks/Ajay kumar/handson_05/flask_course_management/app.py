from flask import Flask
from flask_migrate import Migrate

from config import Config
from courses.models import db
from courses.routes import course_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate = Migrate(app, db)

    app.register_blueprint(course_bp)

    return app

app = create_app()