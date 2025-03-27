from backend.database.database import get_engine
from backend.database.database_model import Base
from backend.utils.logger import logger  # Importar el logger

def init_db():
    """Inicializa la base de datos creando las tablas definidas en los modelos."""
    try:
        # Crear el motor de la base de datos
        engine = get_engine()
        logger.info("Conectando a la base de datos...")
        # Crear todas las tablas basadas en los modelos de SQLAlchemy

        Base.metadata.create_all(bind=engine)
        logger.info("Base de datos inicializada con éxito.")

    except Exception as e:
        logger.critical(f"Error al inicializar la base de datos: {str(e)}", exc_info=True)
        raise

