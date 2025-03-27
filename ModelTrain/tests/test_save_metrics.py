import pytest
import json
import numpy as np
import pandas as pd
from pathlib import Path
from model_train.utils.save_metrics import save_metrics  # ✅ Importación correcta
from model_train.configs.config import METRICS_DIR

# Directorio temporal para pruebas
TEST_DIR = METRICS_DIR

@pytest.fixture
def sample_data():
    """Genera datos de prueba: reporte de clasificación y matriz de confusión."""
    report = """              precision    recall  f1-score   support
        Clase_0       0.80      0.85      0.82       100
        Clase_1       0.75      0.70      0.72        50
        accuracy                           0.78       150
       macro avg       0.77      0.77      0.77       150
    weighted avg       0.78      0.78      0.78       150
    """
    matrix = np.array([[85, 15], [15, 35]])  # Matriz de confusión
    return report, matrix

def test_save_metrics(sample_data):
    """Prueba la función save_metrics con diferentes formatos de salida."""
    report, matrix = sample_data

    # Ejecutar la función
    save_metrics(report, matrix, TEST_DIR)

    # Verificar que los archivos se crearon correctamente
    assert (TEST_DIR / "metrics/metrics.txt").exists(), "El archivo TXT no se generó."
    assert (TEST_DIR / "metrics/metrics.csv").exists(), "El archivo CSV no se generó."
    assert (TEST_DIR / "metrics/metrics.json").exists(), "El archivo JSON no se generó."
    assert (TEST_DIR / "metrics/metrics.xlsx").exists(), "El archivo Excel no se generó."

    # Verificar contenido JSON
    with open(TEST_DIR / "metrics/metrics.json", "r") as f:
        data = json.load(f)
        assert "classification_report" in data, "El JSON no contiene el reporte de clasificación."
        assert "confusion_matrix" in data, "El JSON no contiene la matriz de confusión."

    # Verificar contenido CSV
    df_csv = pd.read_csv(TEST_DIR / "metrics/metrics.csv", index_col=0)
    assert "Precision" in df_csv.columns, "El CSV no contiene la columna Precision."
    assert "Recall" in df_csv.columns, "El CSV no contiene la columna Recall."

    print("✅ Todas las pruebas pasaron correctamente.")

if __name__ == "__main__":
    pytest.main()
