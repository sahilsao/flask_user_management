from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "users.login"


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename):
    # Create the application instance (app) of the Flask framework
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    # Flask-Login configuration
    from project.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()

    # Blueprint(s)
    from project.users.routes import users_blueprint

    # Register the Blueprint(s)
    app.register_blueprint(users_blueprint)

    return app
