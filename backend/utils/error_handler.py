from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_400(error):
    return jsonify({"error": "Solicitud incorrecta"}), 400

def handle_401(error):
    return jsonify({"error": "No autorizado"}), 401

def handle_403(error):
    return jsonify({"error": "Acceso prohibido"}), 403

def handle_404(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

def handle_405(error):
    return jsonify({"error": "Método no permitido"}), 405

def handle_422(error):
    return jsonify({"error": "Entidad no procesable", "details": str(error)}), 422

def handle_429(error):
    return jsonify({"error": "Demasiadas solicitudes, intenta más tarde"}), 429

def handle_500(error):
    return jsonify({"error": "Error interno del servidor"}), 500

class CustomException(Exception):
    """Excepción personalizada para manejar errores específicos en la aplicación."""
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

def handle_custom_exception(error):
    return jsonify({"error": error.message}), error.status_code

def handle_http_exception(error):
    """Captura errores HTTP predeterminados de Flask."""
    response = error.get_response()
    response.data = jsonify({"error": error.description}).data
    response.content_type = "application/json"
    return response, error.code
