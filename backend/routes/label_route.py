from flask import Blueprint, request, jsonify
from backend.services.label_service import LabelService

label_bp = Blueprint("label", __name__)

@label_bp.route("/", methods=["POST"])
def create_label():
    """Crea una nueva etiqueta asociada a una predicción"""
    data = request.json
    user_id = request.headers.get("user_id")

    if not all(key in data for key in ["label_name", "prediction_id"]):
        return jsonify({"error": "Faltan datos en la solicitud"}), 400

    result = LabelService.create_label(data["label_name"], data["prediction_id"], user_id)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 201
