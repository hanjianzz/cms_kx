from flask import Blueprint

blue = Blueprint('/', __name__, template_folder='templates', static_folder='static')