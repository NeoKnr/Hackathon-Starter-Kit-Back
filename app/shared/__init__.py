import logging
import os
import sys

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from marshmallow import ValidationError

db: SQLAlchemy = SQLAlchemy()
migrate = Migrate()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    print(f"Using {app.config['DB_NAME']}")

    db.init_app(app)
    if app.config['MIGRATION'] == "1":
        migrate.init_app(app, db)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    url_prefix = "/api"

    from data.admin.controllers import admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    
    from data.dossier.controllers import dossier_blueprint
    app.register_blueprint(dossier_blueprint, url_prefix='/dossier')
    
    from data.entreprise.controllers import entreprise_blueprint
    app.register_blueprint(entreprise_blueprint, url_prefix='/entreprise')
    
    from data.etudiant.controllers import etudiant_blueprint
    app.register_blueprint(etudiant_blueprint, url_prefix='/etudiant')
    
    from data.event.controllers import event_blueprint
    app.register_blueprint(event_blueprint, url_prefix='/event')
    
    from data.formulaire.controllers import formulaire_blueprint
    app.register_blueprint(formulaire_blueprint, url_prefix='/formulaire')
    
    from data.photo.controllers import photo_blueprint
    app.register_blueprint(photo_blueprint, url_prefix='/photo')
    
    from data.promotion.controllers import promotion_blueprint
    app.register_blueprint(promotion_blueprint, url_prefix='/promotion')

    @app.errorhandler(ValidationError)
    def handle_custom_error(error):
        return str(error), 400

    CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        db.create_all()

    return app
