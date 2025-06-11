import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db/database.db')
    app.config['SECRET_KEY'] = 'my_supbasedirer_secret'
    # engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    
    db.init_app(app)
    migrate = Migrate(app, db)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .modeles.apprenant import ModeleApprenant
    @login_manager.user_loader
    def load_user(id_apprenant):
        # repr(ModeleApprenant)
        return ModeleApprenant.query.get(int(id_apprenant))
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app