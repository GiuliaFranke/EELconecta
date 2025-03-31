from flask import Flask

app = Flask(__name__)

from eelconecta import routes
