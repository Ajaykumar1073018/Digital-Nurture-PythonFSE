from flask import Flask, jsonify
from flask_migrate import Migrate
from config import Config
from courses.routes import courses_bp
from courses.models import db

# Initialize the migration instance
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load settings from config.py
    app.config.from_object(Config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(courses_bp)

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)