import cv2
import numpy as np
from skimage.feature import hog
from backend.config import (
    HOG_ORIENTATIONS,
    HOG_PIXELS_PER_CELL,
    HOG_CELLS_PER_BLOCK,
    IMAGE_SIZE,
)
from backend.utils.logger import logger  # Importar el logger centralizado

def extract_hog_feature(image):
    """Extrae características HOG de la imagen en escala de grises."""
    try:
        feature, _ = hog(image,
                         orientations=HOG_ORIENTATIONS,
                         pixels_per_cell=HOG_PIXELS_PER_CELL,
                         cells_per_block=HOG_CELLS_PER_BLOCK,
                         block_norm='L2-Hys',
                         visualize=True)
        logger.info("Características HOG extraídas correctamente.")
        return feature
    except Exception as e:
        logger.error(f"Error al extraer características HOG: {e}", exc_info=True)
        return None

    
def preprocess_imagen(file):
    """Carga, preprocesa y extrae características de la imagen."""
    try:
        file_bytes = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if image is None:
            logger.error(f"Error al cargar la imagen {getattr(file, 'filename', 'desconocida')}")
            return None

        logger.info(f"Imagen {getattr(file, 'filename', 'desconocida')} cargada correctamente.")

        # Convertir a escala de grises
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        logger.info("Imagen convertida a escala de grises.")

        # Redimensionar la imagen
        image = cv2.resize(image, IMAGE_SIZE)
        logger.info(f"Imagen redimensionada a {IMAGE_SIZE}.")

        # Extraer características HOG
        features = extract_hog_feature(image)

        if features is None:
            logger.error(f"Error al extraer características HOG de la imagen {getattr(file, 'filename', 'desconocida')}")
            return None

        logger.info(f"Preprocesamiento de imagen {getattr(file, 'filename', 'desconocida')} completado.")
        return features.reshape(1, -1)

    except Exception as e:
        logger.error(f"Error en preprocess_imagen: {e}", exc_info=True)
        return None
