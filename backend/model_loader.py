from backend.config import MODEL_PATH
import joblib
from backend.utils.logger import logger  # Importar el logger centralizado

def load_model():
    """Carga el modelo desde el archivo especificado en MODEL_PATH."""
    try:
        logger.info(f"Intentando cargar el modelo desde {MODEL_PATH}...")
        model = joblib.load(MODEL_PATH)
        logger.info("Modelo cargado exitosamente.")
        return model

    except FileNotFoundError:
        logger.error(f"Error: No se encontró el archivo del modelo en {MODEL_PATH}.", exc_info=True)
    except joblib.externals.loky.process_executor.BrokenProcessPool:
        logger.error("Error: Fallo en la deserialización del modelo (BrokenProcessPool).", exc_info=True)
    except Exception as e:
        logger.error(f"Error inesperado al cargar el modelo: {e}", exc_info=True)

    return None  # Retorna None si hubo un error

# Cargar el modelo globalmente
model = load_model()

if model is None:
    logger.warning("El modelo no se cargó correctamente. Verifica el archivo y la ruta.")
