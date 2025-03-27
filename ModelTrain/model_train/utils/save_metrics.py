import json
import pandas as pd
from pathlib import Path
from model_train.utils.logger import logger
import numpy as np
import re

def save_txt(report, matrix, path):
    """Guarda el reporte de clasificación y la matriz de confusión en un archivo TXT."""
    try:
        path_text = path / 'metrics'/ 'metrics.txt'
        with open(path_text, "w") as f:
            f.write("### Reporte de Clasificación ###\n")
            f.write(report + "\n\n")
            f.write("### Matriz de Confusión ###\n")
            f.write(str(matrix) + "\n")
        
        logger.info(f"✅ Reporte guardado en TXT: {path_text}")
    except Exception as e:
        logger.error(f"❌ Error al guardar en TXT: {e}")

def save_csv(report, path):
    """Guarda el reporte de clasificación en formato CSV."""
    try:
        report_dict = {}
        lines = report.split("\n")
        if len(lines) > 2:
            for line in lines[2:-3]:  
                row = line.split()
                if len(row) > 0:
                    class_name = row[0]
                    report_dict[class_name] = [float(x) for x in row[1:]]

        df_report = pd.DataFrame.from_dict(report_dict, orient="index",
                                           columns=["Precision", "Recall", "F1-score", "Support"])
        path_csv = path / 'metrics'/  'metrics.csv'
        df_report.to_csv(path_csv, index=True)

        logger.info(f"✅ Reporte guardado en CSV: {path_csv}")
    except Exception as e:
        logger.error(f"❌ Error al guardar en CSV: {e}")

def save_json(report, matrix, path):
    """Guarda el reporte de clasificación y la matriz de confusión en formato JSON."""
    try:
        report_json = {}

        # Extraer datos del reporte
        lines = report.strip().split("\n")
        for line in lines:
            row = re.split(r"\s{2,}", line.strip())  # Divide por múltiples espacios
            if len(row) == 5 and row[0].isalpha():  # Evita líneas incorrectas
                class_name = row[0]
                try:
                    report_json[class_name] = {
                        "precision": float(row[1]),
                        "recall": float(row[2]),
                        "f1-score": float(row[3]),
                        "support": int(row[4])
                    }
                except ValueError:
                    logger.warning(f"⚠️ Error al procesar la fila: {line}")

        # Crear el diccionario final
        data = {
            "classification_report": report_json,
            "confusion_matrix": matrix.tolist() if isinstance(matrix, np.ndarray) else matrix
        }

        # Asegurar que la carpeta "metrics" exista
        path_metrics = Path(path) / "metrics"
        path_metrics.mkdir(parents=True, exist_ok=True)

        # Guardar en JSON
        path_json = path_metrics / "metrics.json"
        with open(path_json, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        logger.info(f"✅ Reporte guardado en JSON: {path_json}")
    except Exception as e:
        logger.error(f"❌ Error al guardar en JSON: {e}")

def save_excel(report, matrix, path):
    """Guarda el reporte de clasificación y la matriz de confusión en formato Excel."""
    try:
        report_dict = {}
        lines = report.split("\n")
        if len(lines) > 2:
            for line in lines[2:-3]:  
                row = line.split()
                if len(row) > 0:
                    class_name = row[0]
                    report_dict[class_name] = [float(x) for x in row[1:]]

        df_report = pd.DataFrame.from_dict(report_dict, orient="index",
                                           columns=["Precision", "Recall", "F1-score", "Support"])
        df_matrix = pd.DataFrame(matrix)

        path_excel = path / 'metrics'/  'metrics.xlsx'
        with pd.ExcelWriter(path_excel) as writer:
            df_report.to_excel(writer, sheet_name="Classification Report")
            df_matrix.to_excel(writer, sheet_name="Confusion Matrix")

        logger.info(f"✅ Reporte guardado en Excel: {path_excel}")
    except Exception as e:
        logger.error(f"❌ Error al guardar en Excel: {e}")

def save_metrics(report, matrix, path):
    """Función principal que guarda el reporte en múltiples formatos."""
    if not isinstance(report, str) or not report.strip():
        raise ValueError("❌ El reporte de clasificación no es válido.")
    if matrix is None or not hasattr(matrix, "tolist"):
        raise ValueError("❌ La matriz de confusión no es válida.")

    # Convertir a objeto Path y crear la carpeta si no existe
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)

    save_txt(report, matrix, path)
    save_csv(report, path)
    save_json(report, matrix, path)
    save_excel(report, matrix, path)