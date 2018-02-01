from flask import Flask


app = Flask(__name__)

# Import the routes defined for this project
from project import routes