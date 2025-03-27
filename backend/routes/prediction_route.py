from flask import Blueprint, request, jsonify
from backend.services.prediction_service import PredictionService
from uuid import UUID
# Crear el Blueprint para las rutas de predicción
prediction_bp = Blueprint("prediction", __name__)

@prediction_bp.route("/", methods=["GET"])
def list_predictions():
    """Ruta de prueba para verificar que el endpoint está activo."""
    return jsonify({"message": "Endpoint de predicción disponible"}), 200

@prediction_bp.route("/predict", methods=["POST"])
def create_prediction():
    """Recibe una imagen, la procesa y devuelve la predicción."""
    if "file" not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    image_file = request.files["file"]
    user_id_str = request.form.get("user_id")
    # Convertir el user_id a UUID
    try:
        user_id = UUID(user_id_str)  # Convertir a UUID
    except ValueError:
        return jsonify({"error": "Formato de user_id inválido"}), 400
    result = PredictionService.create_prediction(image_file, user_id)
    return jsonify(result), 201 if "error" not in result else 400

@prediction_bp.route("/<int:prediction_id>", methods=["GET"])
def get_prediction(prediction_id):
    """Recupera una predicción guardada en la base de datos por ID."""
    result = PredictionService.get_prediction(prediction_id)
    return jsonify(result), 200 if "error" not in result else 404


@prediction_bp.route("/correct", methods=["POST"])
def correct_prediction():
    """Recibe la confirmación del usuario sobre la predicción y la guarda si es incorrecta."""
    try:
        data = request.get_json()
        prediction_id = data.get("prediction_id")
        confirmation = data.get("confirmation")
        correct_mineral = data.get("correctMineral", None)

        if not prediction_id or confirmation not in ["si", "no"]:
            return jsonify({"error": "Datos inválidos"}), 400

        result = PredictionService.correct_prediction(prediction_id, confirmation, correct_mineral)
        return jsonify(result), 200 if "message" in result else 400

    except Exception as e:
        return jsonify({"error": f"Error al registrar corrección: {str(e)}"}), 500

