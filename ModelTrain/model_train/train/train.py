import numpy as np
import joblib
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from model_train.utils.load_data import load_dataset, extract_hog_features
from model_train.train.model import build_classifier
from model_train.train.augmentations import augment_image
from model_train.utils.logger import logger
from model_train.configs.config import (MODEL_SAVE_PATH, 
                                        OUTPUT_DATA_SET_DIR, 
                                        METRICS_DIR, 
                                        CLASSIFIER_TYPE, 
                                        RANDOM_STATE)
from model_train.utils.save_plots import (save_accuracy_plot, 
                                              save_confusion_matrix,
                                              save_loss_plot)
from model_train.utils.save_metrics import save_metrics
def main():
    start_time = time.time()

    # Carga de datos
    try:
        logger.info(f"Cargando datos desde: {OUTPUT_DATA_SET_DIR}")
        images, labels = load_dataset()
        if not images or not labels:
            raise ValueError("Los datos cargados están vacíos.")
    except Exception as e:
        logger.error(f"Error al cargar datos: {e}", exc_info=True)
        return

    # Aumentación de datos
    logger.info("Aplicando aumentaciones a las imágenes...")
    augmented_images = []
    augmented_labels = []

    for img, label in zip(images, labels):
        try:
            augmented = augment_image(img)
            if not augmented:  # Verifica si la lista está vacía
                logger.warning(f"La imagen con etiqueta {label} no generó aumentaciones.")
                continue
            augmented_images.extend(augmented)
            augmented_labels.extend([label] * len(augmented))
        except Exception as e:
            logger.warning(f"Error en aumentación de imagen: {e}", exc_info=True)

    all_images = np.concatenate((images, augmented_images))
    all_labels = np.concatenate((labels, augmented_labels))

    # Extracción de características HOG
    try:
        logger.info("Extrayendo características HOG...")
        features = np.array(list(map(extract_hog_features, all_images)))
        if features.size == 0:
            raise ValueError("No se pudieron extraer características.")
    except Exception as e:
        logger.error(f"Error en la extracción de características: {e}", exc_info=True)
        return

    logger.info(f"Características extraídas exitosamente.")

    # División del dataset
    X_train, X_val, y_train, y_val = train_test_split(features, all_labels, test_size=0.2, random_state=RANDOM_STATE)

    # Entrenamiento del modelo
    try:
        logger.info("Entrenando el modelo...")
        clf = build_classifier()
        clf.fit(X_train, y_train)
    except Exception as e:
        logger.error(f"Error durante el entrenamiento: {e}", exc_info=True)
        return

    logger.info("Entrenamiento del modelo completado.")

    # Evaluación del modelo
    try:
        logger.info("Evaluando el modelo...")
        y_pred = clf.predict(X_val)
        report = classification_report(y_val, y_pred, zero_division=1)
        matrix = confusion_matrix(y_val, y_pred)

        logger.info("Resultados del entrenamiento:")
        logger.info(report)
        logger.info(f"Matriz de confusión:\n{matrix}")

        # Guardar modelo
        joblib.dump(clf, MODEL_SAVE_PATH, compress=3)
        logger.info(f"Modelo guardado en: {MODEL_SAVE_PATH}")
        
        accuracies = [clf.score(X_train, y_train), clf.score(X_val, y_val)]
        losses = [1 - clf.score(X_train, y_train), 1 - clf.score(X_val, y_val)]

        # Guardar results
        save_metrics(report, 
                     matrix, 
                     METRICS_DIR)
        
        save_confusion_matrix(matrix, 
                              labels=list(CLASSIFIER_TYPE),
                              path=METRICS_DIR)
        
        save_accuracy_plot(accuracies=accuracies, 
                           path=METRICS_DIR)
        
        save_loss_plot(losses=losses, 
                        path=METRICS_DIR )
    except Exception as e:
        logger.error(f"Error al evaluar o guardar resultados: {e}", exc_info=True)
        return

    elapsed_time = time.time() - start_time
    logger.info(f"Proceso finalizado en {elapsed_time:.2f} segundos")

