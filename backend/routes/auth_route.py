from flask import Blueprint, request, jsonify
from backend.services.auth_service import AuthServices
from backend.utils.middleware import token_required
from flask_jwt_extended import jwt_required, get_jwt_identity,create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET"])
def list_auths():
    """Ruta de prueba para verificar que el endpoint está activo."""
    return jsonify({"message": "Endpoint de autenticación activo"}), 200

@auth_bp.route('/login', methods=['POST'])
def login():
    """Permite a los usuarios autenticarse y recibir un token JWT."""
    try:
        data = request.get_json()

        # Validar que los campos requeridos estén en la petición
        if not data or "username" not in data or "password" not in data:
            return jsonify({"error": "Faltan credenciales"}), 400

        response, status_code = AuthServices.authenticate(data["username"], data["password"])
        return jsonify(response), status_code

    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@auth_bp.route('/signup', methods=['POST'])
def signup():
    """Registra a un nuevo usuario en la base de datos."""
    try:
        data = request.get_json()
        
        # Validar que se hayan enviado los campos necesarios
        if not data or "username" not in data or "email" not in data or "password" not in data:
            return jsonify({"error": "Faltan datos de registro"}), 400

        # Llamar al servicio de autenticación para crear el usuario
        response, status_code = AuthServices.signup(data["username"], data["email"], data["password"])
        return jsonify(response), status_code

    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@auth_bp.route("/user", methods=["GET"])
def get_user():
    """Endpoint para obtener la información del usuario autenticado."""
    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"error": "Token no proporcionado"}), 401

    # Extraer solo el token sin 'Bearer '
    token = token.replace("Bearer ", "")

    response, status_code = AuthServices.get_user(token)
    return jsonify(response), status_code



@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)  # Solo permite tokens de "refresh"
def refresh_token():
    """Genera un nuevo token de acceso usando el refresh token"""
    user_id = get_jwt_identity()
    new_access_token = create_access_token(identity=user_id)
    return jsonify({"token": new_access_token}), 200