from flask import Blueprint

from app.controllers.cachorro_controller import create_dog

bp_dogs = Blueprint("bp_dogs", __name__, url_prefix="/dogs")
bp_dogs.post("")(create_dog)