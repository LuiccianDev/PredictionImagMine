import cv2
from .logger import logger
from skimage.feature import hog
from model_train.configs.config import (HOG_ORIENTATIONS, 
                                        HOG_PIXELS_PER_CELL, 
                                        HOG_CELLS_PER_BLOCK,
                                        OUTPUT_DATA_SET_DIR)




def load_dataset():
    """Carga las imágenes del dataset y devuelve las imágenes y etiquetas."""
    
    logger.info("Inicializando la carga de datos...")
    data = []
    labels = []
    
    # Verificar si el directorio existe
    if not OUTPUT_DATA_SET_DIR.exists():
        logger.error(f"El directorio {OUTPUT_DATA_SET_DIR} no existe.")
        return data, labels

    # Iterar sobre las clases (subdirectorios)
    for class_path in sorted(OUTPUT_DATA_SET_DIR.iterdir()):
        if class_path.is_dir():
            logger.info(f"Procesando clase: {class_path.name}")

            # Iterar sobre las imágenes en cada clase
            for img_path in class_path.iterdir():
                try:
                    # Verificar si es una imagen válida
                    if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                        image = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)

                        if image is not None:
                            data.append(image)
                            labels.append(class_path.name)
                            logger.debug(f"Imagen cargada correctamente: {img_path}")
                        else:
                            logger.warning(f"No se pudo cargar la imagen: {img_path}")
                    else:
                        logger.debug(f"Archivo no soportado (omitido): {img_path}")

                except Exception as e:
                    logger.error(f"Error al cargar la imagen {img_path}: {e}")

    logger.info(f"Finalizó la carga del dataset. Total imágenes: {len(data)}")
    return data, labels

                    
def extract_hog_features(img):
    try :
        feature = hog(img,
                        orientations=HOG_ORIENTATIONS,
                        pixels_per_cell=HOG_PIXELS_PER_CELL,
                        cells_per_block=HOG_CELLS_PER_BLOCK,
                        block_norm='L2-Hys',
                        visualize=False)
        return feature
    
    except Exception as e : 
        logger.error(f"Error en la extraccion de caracteristicas HOG : {e}")
        return None
    
