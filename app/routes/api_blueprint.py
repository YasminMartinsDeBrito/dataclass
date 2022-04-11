from flask import Blueprint

from app.routes.cachorro_blueprint import bp_dogs

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

bp_api.register_blueprint(bp_dogs)