import argparse

import time
import model_train  # Asegura que `model_train` sea un paquete con __init__.py
from model_train import logger


def run_pipeline():
    """Ejecuta la carga, procesamiento de datos y el entrenamiento del modelo."""
    logger.info("Inicio del pipeline de datos y entrenamiento...")
    
    logger.info("Esperando 1 minuto antes de procesar los datos...")
    time.sleep(60)  # Espera de 1 minuto
    
    try:
        model_train.preprocess_data()
        logger.info("Procesamiento de datos completado correctamente.")
    except Exception as e:
        logger.error(f"Error en el procesamiento de datos: {e}")
    
    logger.info("Esperando 2 minutos después de procesar los datos...")
    time.sleep(120)  # Espera de 2 minutos

    try:
        model_train.main()
        logger.info("Ejecución del modelo completada correctamente.")
    except Exception as e:
        logger.error(f"Error en la ejecución del modelo: {e}")

    logger.info("Fin del proceso.")

def main():
    """Procesa los argumentos CLI."""
    parser = argparse.ArgumentParser(description="Ejecutar funciones del paquete src")
    parser.add_argument("--run", action="store_true", help="Ejecuta el pipeline completo (procesamiento + entrenamiento)")
    
    args = parser.parse_args()

    if args.run:
        run_pipeline()

if __name__ == "__main__":
    main()



#! run Script comado ejecuta el main() de train  y el preprocessinff _data 
 #* python -m model_train --run 
