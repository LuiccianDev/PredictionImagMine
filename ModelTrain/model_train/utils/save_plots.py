import matplotlib
matplotlib.use("Agg")  # Usa un backend sin interfaz gráfica

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from PIL import Image
import numpy as np
from model_train.utils.logger import logger

def save_plot_as_image(fig, path):
    """Convierte una figura de matplotlib en imagen PIL y la guarda sin depender de tkinter."""
    try:
        fig.canvas.draw()  # Renderiza la figura
        buf = fig.canvas.buffer_rgba()  # Obtiene el buffer RGBA
        img = Image.fromarray(np.asarray(buf))  # Convierte a imagen PIL
        path.parent.mkdir(parents=True, exist_ok=True)  # Crea directorios si no existen
        img.save(path, format="PNG")  # Guarda la imagen
        plt.close(fig)  # Cierra la figura
        logger.info(f"✅ Imagen guardada en: {path}")
    except Exception as e:
        logger.error(f"❌ Error en `save_plot_as_image`: {e}")

def save_accuracy_plot(accuracies, path):
    try:
        if not accuracies or not isinstance(accuracies, (list, tuple)):
            raise ValueError("La lista de accuracies está vacía o no es válida.")
        
        path_img = Path(path) / 'imgs' / 'accuracy_plot.png'
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(range(1, len(accuracies) + 1), accuracies, marker='o', linestyle='-', color='b', label="Accuracy")
        ax.set_title('Precisión del Modelo')
        ax.set_ylabel('Precisión')
        ax.set_xlabel('Épocas')
        ax.grid(True)
        ax.legend()
        
        save_plot_as_image(fig, path_img)
    except Exception as e:
        logger.error(f"❌ Error en `save_accuracy_plot`: {e}")

def save_loss_plot(losses, path):
    try:
        if not losses or not isinstance(losses, (list, tuple)):
            raise ValueError("La lista de pérdidas está vacía o no es válida.")
        
        path_img = Path(path) / 'imgs' / 'loss_plot.png'
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(range(1, len(losses) + 1), losses, marker='o', linestyle='-', color='r', label="Loss")
        ax.set_xlabel('Épocas')
        ax.set_ylabel('Pérdida (Loss)')
        ax.set_title('Evolución de la Pérdida por Época')
        ax.grid(True)
        ax.legend()
        
        save_plot_as_image(fig, path_img)
    except Exception as e:
        logger.error(f"❌ Error en `save_loss_plot`: {e}")

def save_confusion_matrix(matrix, labels, path):
    try:
        if matrix is None or not hasattr(matrix, "__iter__"):
            raise ValueError("La matriz de confusión no es válida.")
        if not isinstance(labels, (list, tuple)) or not labels:
            raise ValueError("Las etiquetas no son válidas.")
        
        path_img = Path(path) / 'imgs' / 'confusion_matrix_plot.png'
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(matrix, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels, ax=ax)
        ax.set_xlabel('Predicciones')
        ax.set_ylabel('Valores Reales')
        ax.set_title('Matriz de Confusión')
        
        save_plot_as_image(fig, path_img)
    except Exception as e:
        logger.error(f"❌ Error en `save_confusion_matrix`: {e}")


""" def save_metrics(report, matrix, path_metrics):
    try:
        if not isinstance(report, str) or not report.strip():
            raise ValueError("El reporte de clasificación no es válido.")
        if matrix is None:
            raise ValueError("La matriz de confusión no es válida.")

        path_metrics = Path(path_metrics)
        path_metrics.parent.mkdir(parents=True, exist_ok=True)

        with open(path_metrics, 'w') as f:
            f.write("Reporte de Clasificación:\n")
            f.write(report + "\n\n")
            f.write("Matriz de Confusión:\n")
            f.write(str(matrix) + "\n")

        print(f"✅ Reporte de métricas guardado en: {path_metrics}")

    except Exception as e:
        print(f"❌ Error en `save_metrics`: {e}") """