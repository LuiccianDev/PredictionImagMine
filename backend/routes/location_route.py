from flask import Blueprint, request, jsonify
from backend.services.location_service import LocationService

location_bp = Blueprint("location", __name__)

@location_bp.route("/", methods=["POST"])
def create_location():
    """Crea una nueva ubicación asociada al usuario"""
    data = request.json
    user_id = request.headers.get("user_id")

    if "location_name" not in data:
        return jsonify({"error": "Falta el nombre de la ubicación"}), 400

    result = LocationService.create_location(data["location_name"], user_id)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201
