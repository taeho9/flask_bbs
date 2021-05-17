from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .pages import main_page
    from .pages import sub_page
    app.register_blueprint(main_page.bp)
    #app.register_blueprint(sub_page.bp1)

    return app

