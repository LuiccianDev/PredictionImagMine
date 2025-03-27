import logging
import os
import pathlib
from logging.handlers import RotatingFileHandler

try:
    import colorlog  # Para logs en color en consola si está disponible
    COLORLOG_AVAILABLE = True
except ImportError:
    COLORLOG_AVAILABLE = False

from backend.config import LOGGING_FILE

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / LOGGING_FILE

def setup_logger(name="backend", log_file=CONFIG_PATH, level=None, max_bytes=5*1024*1024, backup_count=3):
    """
    Configura el logger con:
    - Consola con colores (si está disponible `colorlog`)
    - Archivo de logs con rotación automática
    - Nivel de log configurable (por parámetro o variable de entorno)
    - Formato de timestamp detallado
    """
    
    # Evitar que se agreguen múltiples handlers si el logger ya existe
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # Si ya tiene handlers, usar el existente

    # Nivel de log (prioridad: parámetro > variable de entorno > INFO por defecto)
    level = level or os.getenv("LOG_LEVEL", "INFO").upper()
    logger.setLevel(level)

    # Formato de logs
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S"
    )

    # Handler para archivo con rotación
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para consola con colores (si `colorlog` está disponible)
    if COLORLOG_AVAILABLE:
        console_formatter = colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(message)s",
            datefmt="%d-%b-%y %H:%M:%S",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red'
            }
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger

# Inicializar logger
logger = setup_logger()

