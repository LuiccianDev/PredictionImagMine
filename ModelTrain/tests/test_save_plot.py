import pytest
import numpy as np
from pathlib import Path
from model_train.utils.save_plots import (
    save_accuracy_plot,
    save_loss_plot,
    save_confusion_matrix
)
from model_train.configs.config import METRICS_DIR, CLASSIFIER_TYPE
# Directorio temporal para pruebas
TEST_DIR = METRICS_DIR


@pytest.fixture
def sample_data():
    accuracies = [0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.5]
    losses = [1.2, 0.9, 0.7, 0.5, 0.3]
    confusion_matrix = np.array([[50, 10, 5], [8, 60, 7], [3, 9, 70]])
    labels = list(CLASSIFIER_TYPE)
    return accuracies, losses, confusion_matrix, labels


def test_save_accuracy_plot(sample_data):
    accuracies, _, _, _ = sample_data
    save_accuracy_plot(accuracies, TEST_DIR)
    assert (TEST_DIR / "imgs" / "accuracy_plot.png").exists(), "El gráfico de precisión no se generó."


def test_save_loss_plot(sample_data):
    _, losses, _, _ = sample_data
    save_loss_plot(losses, TEST_DIR)
    assert (TEST_DIR / "imgs" / "loss_plot.png").exists(), "El gráfico de pérdida no se generó."


def test_save_confusion_matrix(sample_data):
    _, _, confusion_matrix, labels = sample_data
    save_confusion_matrix(confusion_matrix, labels, TEST_DIR)
    assert (TEST_DIR / "imgs" / "confusion_matrix_plot.png").exists(), "El gráfico de la matriz de confusión no se generó."
