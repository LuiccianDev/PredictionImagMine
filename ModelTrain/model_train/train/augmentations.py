import cv2
import random
import numpy as np
from model_train.utils.logger import logger


def validate_image(img, func_name="función"):
    """
    Valida que 'img' sea un numpy.ndarray y no sea None.
    Si la validación falla, registra un error y lanza una excepción.
    """
    if img is None or not isinstance(img, np.ndarray):
        logger.error(f"{func_name}: La imagen es inválida. Debe ser un numpy.ndarray.")
        raise ValueError("La imagen debe ser un numpy.ndarray válido.")

def flip_horizontal(img):
    """
    Voltea la imagen horizontalmente.
    """
    validate_image(img, "flip_horizontal")
    return cv2.flip(img, 1)

def rotate_image(img, angle=15):
    """
    Rota la imagen un ángulo fijo (por defecto 15°).
    """
    validate_image(img, "rotate_image")
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    return rotated

def rotate_image_random(img, max_angle=15):
    """
    Rota la imagen un ángulo aleatorio entre -max_angle y +max_angle.
    """
    validate_image(img, "rotate_image_random")
    angle = random.randint(-max_angle, max_angle)
    logger.info("Rotación aleatoria de %s grados", angle)
    return rotate_image(img, angle)

def translate_image(img, tx=10, ty=-10):
    """
    Desplaza la imagen tx en x y ty en y.
    """
    validate_image(img, "translate_image")
    (h, w) = img.shape[:2]
    M = np.float32([[1, 0, tx],
                    [0, 1, ty]])
    shifted = cv2.warpAffine(img, M, (w, h))
    return shifted

def scale_image(img, scale_min=0.9, scale_max=1.1):
    """
    Escala la imagen aleatoriamente entre [scale_min, scale_max].
    """
    validate_image(img, "scale_image")
    (h, w) = img.shape[:2]
    scale = random.uniform(scale_min, scale_max)
    logger.info("Escalando imagen con factor: %s", scale)
    M = np.float32([[scale, 0,      0],
                    [0,     scale,  0]])
    scaled = cv2.warpAffine(img, M, (w, h))
    return scaled

def add_gaussian_noise(img, sigma=10):
    """
    Añade ruido gaussiano con desviación estándar 'sigma'.
    """
    validate_image(img, "add_gaussian_noise")  # Asegurar que la imagen es válida
    
    noise = np.random.normal(0, sigma, img.shape).astype(np.uint8)  # Convertir a uint8
    noisy = cv2.add(img, noise, dtype=cv2.CV_8U)  # Especificar tipo de salida
    
    return noisy

def augment_image(img):
    """
    Genera varias versiones aumentadas de 'img' y las devuelve en una lista:
      1) Imagen original
      2) Flip horizontal
      3) Rotación aleatoria entre -15 y 15
    """
    validate_image(img, "augment_image")
    augmented = []
    
    # 1) Imagen original
    augmented.append(img)

    # 2) Flip horizontal
    flipped = flip_horizontal(img)
    augmented.append(flipped)
    
    # 3) Rotación aleatoria entre -15 y 15
    rotated_rand = rotate_image_random(img, max_angle=15)
    augmented.append(rotated_rand)
    
    return augmented
