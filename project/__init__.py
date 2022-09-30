from click import echo
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


# -------------
# Configuration
# -------------

# Create a naming convention for the database tables
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy(metadata=metadata)
login = LoginManager()
login.login_view = "users.login"


# ----------------------------
# Application Factory Function
# ----------------------------

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    initialize_extensions(app)
    register_blueprints(app)
    register_cli_commands(app)
    return app


# ----------------
# Helper Functions
# ----------------

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    login.init_app(app)

    # Flask-Login configuration
    from project.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from project.recipes import recipes_blueprint
    from project.users import users_blueprint

    app.register_blueprint(recipes_blueprint)
    app.register_blueprint(users_blueprint)


def register_cli_commands(app):
    @app.cli.command('init_db')
    def initialize_database():
        """Initialize the SQLite database."""
        db.drop_all()
        db.create_all()
        echo('Initializing the SQLite database!')

