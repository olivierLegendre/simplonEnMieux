import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()


def create_app() -> Flask:
    """
    Initialise l'application flask
    Configure la base de donnée et le "secret"
    Initialise le login_manager et flask_migrate
    Met en place deux blueprints main et auth
    Returns:
        Flask: _description_
    """
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        basedir, "db/database.db"
    )
    app.config["SECRET_KEY"] = "my_supbasedirer_secret"

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from .modeles.apprenant_certification import ModeleApprenant

    @login_manager.user_loader
    def load_user(id_apprenant):
        return ModeleApprenant.query.get(int(id_apprenant))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
