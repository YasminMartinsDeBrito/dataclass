from flask import request, current_app, jsonify
from app.models.cachorro_model import CachorroModel

def create_dog():
    data = request.get_json()

    new_dog = CachorroModel(**data)

    current_app.db.session.add(new_dog)
    current_app.db.session.commit()

    return jsonify(new_dog), 201