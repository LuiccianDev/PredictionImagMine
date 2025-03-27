import cv2
import joblib
import logging
import os
from skimage.feature import hog
from model_train.configs.config import (
    HOG_ORIENTATIONS,
    HOG_PIXELS_PER_CELL,
    HOG_CELLS_PER_BLOCK,
    IMAGE_SIZE,
    MODEL_PATH
)

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def extract_hog_feature(image):
    try:
        feature, _ = hog(image,
                         orientations=HOG_ORIENTATIONS,
                         pixels_per_cell=HOG_PIXELS_PER_CELL,
                         cells_per_block=HOG_CELLS_PER_BLOCK,
                         block_norm='L2-Hys',
                         visualize=True)
        return feature
    except Exception as e:
        logging.error(f"Error al extraer características HOG: {e}", exc_info=True)
        return None

def predict_image(image_path):
    # Verificar si la ruta del archivo es válida
    if not os.path.exists(image_path):
        logging.error(f"El archivo {image_path} no existe")
        raise FileNotFoundError(f"El archivo {image_path} no existe")

    # Cargar la imagen
    image = cv2.imread(image_path)

    # Verificar si la imagen se cargó correctamente
    if image is None:
        logging.error(f"No se pudo cargar la imagen: {image_path}")
        raise ValueError(f"No se pudo cargar la imagen: {image_path}")

    # Convertir a escala de grises
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, IMAGE_SIZE)

    # Extraer características HOG
    features = extract_hog_feature(image)
    
    if features is None or len(features) == 0:
        logging.error("Error al extraer características HOG")
        raise ValueError("Error al extraer características HOG")

    features = features.reshape(1, -1)
    if not os.path.exists(MODEL_PATH):
        logging.error(f"El modelo no se encontró en {MODEL_PATH}")
        raise FileNotFoundError(f"El modelo no se encontró en {MODEL_PATH}")
    # Cargar modelo
    model = joblib.load(MODEL_PATH)
    prediction = model.predict(features)
    # Manejar predict_proba si está disponible
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)
        confidence = max(probabilities[0])
    else:
        logging.warning("El modelo no admite predict_proba, usando 1.0 como confianza")
        confidence = 1.

    return prediction[0], confidence
