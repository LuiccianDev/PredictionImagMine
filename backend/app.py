from flask import Flask, jsonify
from flask_cors import CORS
from backend.routes import register_blueprints
from backend.utils.logger import logger  # Importamos el logger centralizado
from backend.utils.error_handler import (
    handle_400, handle_401, handle_403, handle_404, 
    handle_405, handle_422, handle_429, handle_500, 
    handle_custom_exception, handle_http_exception, CustomException
)
from backend.database.init_db import init_db
from backend.config import SECRET_KEY
def register_error_handlers(app):
    """Registra los manejadores de errores en la aplicación Flask."""
    app.register_error_handler(400, handle_400)
    app.register_error_handler(401, handle_401)
    app.register_error_handler(403, handle_403)
    app.register_error_handler(404, handle_404)
    app.register_error_handler(405, handle_405)
    app.register_error_handler(422, handle_422)
    app.register_error_handler(429, handle_429)
    app.register_error_handler(500, handle_500)
    app.register_error_handler(CustomException, handle_custom_exception)
    app.register_error_handler(Exception, handle_http_exception)  # Captura excepciones generales

def create_app():
    """Inicializa la aplicación Flask."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    # Registrar rutas
    register_blueprints(app)

    @app.route('/')
    def home():
        logger.info("Ruta '/' accedida correctamente.")
        return jsonify({"message": "La aplicación Flask ha iniciado correctamente!"})

    # Registrar manejadores de errores
    register_error_handlers(app)

    # Inicializar base de datos
    try:
        init_db()
        logger.info("Base de datos inicializada correctamente.")
    except Exception as e:
        logger.error(f"Error al inicializar la base de datos: {e}", exc_info=True)

    return app