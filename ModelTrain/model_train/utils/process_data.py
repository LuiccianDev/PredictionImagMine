
from .logger import logger
import cv2
from model_train.configs.config import INPUT_DATA_SET_DIR, OUTPUT_DATA_SET_DIR, IMAGE_SIZE,VALID_CLASSES

try :
    OUTPUT_DATA_SET_DIR.mkdir(parents=True, exist_ok=True) 
except Exception as e :
    logger.error(f"Nop se pudo crear el directorio {OUTPUT_DATA_SET_DIR} : {e}", exc_info=True)
    raise

def preprocess_data ():
    try :
        classes = sorted(INPUT_DATA_SET_DIR.iterdir())
    except FileNotFoundError:
        logger.error("No se encontró la carpeta de datos de entrada")
        return
    except Exception as e :
        logger.error(f"Error al leer la carpeta de datos de entrada : {e}", exc_info=True)
        return

    for class_path  in classes:
        if class_path.is_dir() :
            class_name = class_path.name

            #  Verificar si la carpeta pertenece a una clase válida
            if class_name not in VALID_CLASSES:
                logger.warning(f"La carpeta '{class_name}' no es una clase válida. Se omitirá.")
                continue  # Saltar esta carpeta y seguir con la siguiente

            output_class_dir = OUTPUT_DATA_SET_DIR / class_name
            
            try :
                output_class_dir.mkdir(parents=True, exist_ok=True) #crea carpeta por clase
            except Exception as e :
                logger.error(f"No se pudo crear la carpeta {output_class_dir} : {e}", exc_info=True)
                continue
                
            for img_path in class_path.iterdir():
                if img_path.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                    try :
                        image = cv2.imread(str(img_path))
                        if image is None:
                            logger.warning(f"No se pudo cargar la imagen {img_path}")
                            continue
            
                        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        gray_image = cv2.resize(gray_image, IMAGE_SIZE)
                        
                        output_path = output_class_dir / img_path.name
                        success = cv2.imwrite(str(output_path), gray_image)
                        
                        if success  :
                            logger.info(f"Imagen procesada y guardada en {output_path}")
                        
                        else:
                            logger.error(f"No se pudo guardar la imagen {img_path}")
                    except Exception as e:
                        logger.error(f"Error procesando la imagen {img_path} : {e}", exc_info=True)
                        
                else :
                    logger.debug(f"Archivo no soportado (saltado) : {img_path}")