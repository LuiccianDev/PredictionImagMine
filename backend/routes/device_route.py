from flask import Blueprint, request, jsonify
from backend.services.device_service import DeviceService

device_bp = Blueprint("device", __name__)

@device_bp.route("/", methods=["POST"])
def create_device():
    """Crea un nuevo dispositivo asociado al usuario"""
    data = request.json
    user_id = request.headers.get("user_id")

    if "device_name" not in data:
        return jsonify({"error": "Falta el nombre del dispositivo"}), 400

    result = DeviceService.create_device(data["device_name"], user_id)
    
    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201
