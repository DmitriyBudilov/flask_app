from flask import Flask
import os
import config

app = Flask(__name__)
#app.config.from_object(config.Config)

from app import routes

