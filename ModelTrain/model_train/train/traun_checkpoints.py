import numpy as np
import joblib
import time
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from model_train.utils.load_data import load_dataset, extract_hog_features
from train.model import build_classifier
from model_train.utils.logger import logger
from model_train.configs.config import OUTPUT_DATA_SET_DIR, CLASSIFIER_TYPE
from model_train.utils.save_plots import save_accuarcy_plot, save_confusion_matrix, save_loss_plot, save_metrics

# Carpeta de checkpoints
CHECKPOINT_DIR = Path("checkpoints")
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

# Definir los puntos en los que se guardarán los checkpoints (exactamente 5)
CHECKPOINT_EPOCHS = [1, 3, 5, 7, 10]

def save_checkpoint(model, epoch, X_train, y_train, X_val, y_val):
    """ Guarda el modelo y las métricas en una carpeta específica por epoch. """
    epoch_dir = CHECKPOINT_DIR / f"epoch_{epoch}"
    metrics_dir = epoch_dir / "metrics"

    epoch_dir.mkdir(parents=True, exist_ok=True)  # Crear carpeta del epoch
    metrics_dir.mkdir(parents=True, exist_ok=True)  # Crear carpeta de métricas

    # Guardar el modelo como checkpoint
    checkpoint_path = epoch_dir / f"checkpoint_epoch_{epoch}.joblib"
    joblib.dump(model, checkpoint_path)
    logger.info(f"✅ Checkpoint guardado en: {checkpoint_path}")

    # Evaluación del modelo y generación de métricas
    y_pred = model.predict(X_val)
    report = classification_report(y_val, y_pred, zero_division=1)
    matrix = confusion_matrix(y_val, y_pred)

    # Guardar métricas en un archivo de texto
    metrics_path = metrics_dir / "metrics.txt"
    with open(metrics_path, 'w') as f:
        f.write(report + "\n")
        f.write(str(matrix) + "\n")

    logger.info(f"📊 Métricas guardadas en: {metrics_path}")

    # Guardar gráficos en la carpeta del epoch
    save_metrics(report, matrix, metrics_dir / "metrics_plot.png")
    save_confusion_matrix(matrix, labels=list(CLASSIFIER_TYPE), image_path=metrics_dir / "confusion_matrix.png")
    save_accuarcy_plot([model.score(X_train, y_train), model.score(X_val, y_val)], image_path=metrics_dir / "accuracy_plot.png")
    save_loss_plot([1 - model.score(X_train, y_train), 1 - model.score(X_val, y_val)], image_path=metrics_dir / "loss_plot.png")

def main():
    start_time = time.time()

    # Carga de datos
    try:
        logger.info(f"📂 Cargando datos desde: {OUTPUT_DATA_SET_DIR}")
        images, labels = load_dataset()
        if not images or not labels:
            raise ValueError("❌ Los datos cargados están vacíos.")
    except Exception as e:
        logger.error(f"❌ Error al cargar datos: {e}", exc_info=True)
        return

    # División del dataset
    X_train, X_val, y_train, y_val = train_test_split(images, labels, test_size=0.2, random_state=42)

    # Entrenamiento del modelo con checkpoints en 5 epochs específicas
    try:
        logger.info("🚀 Iniciando entrenamiento del modelo...")
        clf = build_classifier()

        num_epochs = 10  # Número total de epochs
        for epoch in range(1, num_epochs + 1):
            logger.info(f"🔹 Epoch {epoch} en progreso...")

            # Extraer características HOG
            features = np.array(list(map(extract_hog_features, X_train)))
            if features.size == 0:
                logger.error(f"❌ No se pudieron extraer características en el epoch {epoch}. Saltando...")
                continue  # Evita entrenar con datos vacíos

            # Entrenar modelo
            clf.fit(features, y_train)

            # Guardar checkpoint solo en los epochs definidos
            if epoch in CHECKPOINT_EPOCHS:
                logger.info(f"💾 Guardando checkpoint en epoch {epoch}...")
                save_checkpoint(clf, epoch, X_train, y_train, X_val, y_val)

    except Exception as e:
        logger.error(f"❌ Error durante el entrenamiento: {e}", exc_info=True)
        return

    logger.info("✅ Entrenamiento del modelo completado.")

    elapsed_time = time.time() - start_time
    logger.info(f"🕒 Proceso finalizado en {elapsed_time:.2f} segundos")

if __name__ == "__main__":
    main()
