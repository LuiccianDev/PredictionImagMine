import yaml
import pathlib
import secrets

DIR_PATH = pathlib.Path(__file__).resolve().parent.parent

CONFIG_YAML_PATH = DIR_PATH / "backend" / "config.yaml"

# Cargar configuración desde config.yaml
def load_config():
    with open(CONFIG_YAML_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# Configuración global
config = load_config()

# Parámetros generales
""" SECRET_KEY = config["secret_key"] """
SECRET_KEY = secrets.token_hex(32)
DEBUG = config["debug"]
HOST = config["host"]
PORT = config["port"]

# Configuración de base de datos
db_type = config["database_type"]
if db_type == "sqlite":
    DATABASE_URI = f"sqlite:///{config['sqlite_db']}"
elif db_type == "mysql":
    DATABASE_URI = (
        f"mysql+pymysql://{config['mysql']['user']}:{config['mysql']['password']}"
        f"@{config['mysql']['host']}:{config['mysql']['port']}/{config['mysql']['dbname']}"
        f"?charset={config['mysql']['charset']}"
    )
elif db_type == "postgres":
    DATABASE_URI = (
        f"postgresql://{config['postgres']['user']}:{config['postgres']['password']}"
        f"@{config['postgres']['host']}:{config['postgres']['port']}/{config['postgres']['dbname']}"
        f"?sslmode={config['postgres']['sslmode']}"
    )
else:
    raise ValueError("Tipo de base de datos no soportado")

# Configuración de logging
LOGGING_LEVEL = config["logging"]["level"]
LOGGING_FILE = DIR_PATH / config["logging"]["file"]

# Configuración de CORS
CORS_ENABLED = config["cors"]["enabled"]
CORS_ORIGINS = config["cors"]["origins"]

# Configuración de seguridad
TOKEN_EXPIRATION = config["security"]["access_token_expiration"]
REFRESH_TOKEN_EXPIRATION = config["security"]["refresh_token_expiration"]
HASHING_ALGORITHM = config["security"]["hashing_algorithm"]

# Configuración de subida de archivos
UPLOAD_FOLDER = config["upload"]["upload_folder"]
ALLOWED_EXTENSIONS = set(config["upload"]["allowed_extensions"])
MAX_CONTENT_LENGTH = config["upload"]["max_size"] * 1024 * 1024

# Configuración de la API de inferencia
MODEL_PATH = DIR_PATH / config["inference"]["model_path"]
BATCH_SIZE = config["inference"]["batch_size"]
IMAGE_SIZE = tuple(config["inference"]["image_size"])


HOG_ORIENTATIONS = config["hog"]["orientations"]
HOG_PIXELS_PER_CELL = tuple(config["hog"]["pixels_per_cell"])
HOG_CELLS_PER_BLOCK = tuple(config["hog"]["cells_per_block"])
