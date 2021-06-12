import os
from flask import Flask
from apps.search_microservice import srch

# Flask app creation
app = Flask(__name__)

# register blueprint
app.register_blueprint(srch)