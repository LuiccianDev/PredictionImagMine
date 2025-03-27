from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.services.user_services import UserService

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()  # Requiere autenticación con JWT
def get_profile():
    try:
        # Obtener el ID del usuario autenticado desde el token JWT
        user_id = get_jwt_identity()

        # Usar el servicio para obtener la información del perfil
        user_profile = UserService.get_user_profile(user_id)
        if not user_profile:
            return jsonify({"error": "Usuario no encontrado"}), 404

        return jsonify(user_profile), 200

    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()  # Requiere autenticación con JWT
def update_profile():
    try:
        # Obtener el ID del usuario autenticado desde el token JWT
        user_id = get_jwt_identity()

        # Obtener los datos de la solicitud
        data = request.get_json()
        if not data or "username" not in data or "email" not in data:
            return jsonify({"error": "Faltan datos de actualización"}), 400

        # Usar el servicio para actualizar el perfil
        updated_profile = UserService.update_user_profile(
            user_id,
            data["username"],
            data["email"]
        )
        if not updated_profile:
            return jsonify({"error": "Usuario no encontrado"}), 404

        return jsonify({"message": "Perfil actualizado exitosamente", "user": updated_profile}), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500