import yaml
import pathlib
from model_train.utils.logger import logger

def load_config():
    try : 
        BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
        CONFIG_PATH = BASE_DIR / "model_train" / "configs" / "config.yaml"

        if not CONFIG_PATH.exists():
            raise FileNotFoundError(f"Archivo de configuración no encontrado: {CONFIG_PATH}")

        with open(CONFIG_PATH, mode='r') as config_file:
            return yaml.safe_load(config_file)
    except yaml.YAMLError as e:
        logger.error(f"Error al leer el archivo de configuración: {e}")
        return None
    except Exception as e:
        logger.error(f"Error inesperado durante la carga de la configuración: {e}")
        return None
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
CONFIG = load_config()

# Definimos constantes basadas en la configuración cargada
IMAGE_SIZE = tuple(CONFIG["image_size"])
CLASSIFIER_TYPE = CONFIG["classifier_type"]
HOG_ORIENTATIONS = CONFIG["hog"]["orientations"]
HOG_PIXELS_PER_CELL = tuple(CONFIG["hog"]["pixels_per_cell"])
HOG_CELLS_PER_BLOCK = tuple(CONFIG["hog"]["cells_per_block"])

INPUT_DATA_SET_DIR = BASE_DIR / CONFIG["paths"]["input_data_set_dir"]
OUTPUT_DATA_SET_DIR = BASE_DIR / CONFIG["paths"]["output_data_set_dir"]
METRICS_DIR = BASE_DIR / CONFIG["paths"]["metrics_dir"]
MODEL_SAVE_PATH = BASE_DIR / CONFIG["paths"]["model_save_path"]
MODEL_PATH = BASE_DIR / CONFIG["paths"]["model_path"]

RANDOM_STATE = CONFIG["random_state"]
VALID_CLASSES = set(CONFIG["valid_classes"])

logger.info("Cargando configuración exitosa.")
