from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.config import DATABASE_URI  # URL de conexión definida en config.py
from backend.utils.logger import logger  # Importar el logger

def get_engine():
    """Función para obtener el motor de la base de datos según la configuración."""
    try:
        logger.info("Inicializando motor de base de datos...")
        engine = create_engine(DATABASE_URI)  # Se obtiene la URL desde config.py
        logger.info("Motor de base de datos inicializado correctamente.")
        return engine
    except Exception as e:
        logger.error(f"Error al inicializar el motor de la base de datos: {str(e)}")
        raise  # Relanza la excepción para que el sistema maneje el error

# Crear una fábrica de sesiones
try:
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    logger.info("Fábrica de sesiones creada correctamente.")
except Exception as e:
    logger.critical(f"Error crítico al crear la sesión de base de datos: {str(e)}")
    raise  # Detiene la ejecución si no se puede conectar a la base de datos
