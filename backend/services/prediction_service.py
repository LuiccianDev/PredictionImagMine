import uuid
from backend.database.database import SessionLocal
from backend.models.prediction import PredictionPostgres
from backend.preprocess import preprocess_imagen
from backend.model_loader import model as MODEL
from backend.utils.logger import logger  
import time

# Extensiones permitidas
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

class PredictionService:
    @staticmethod
    def create_prediction(image_file, user_id=None):
        """Preprocesa la imagen, hace la predicción y almacena el resultado en la BD."""
        try:
            logger.info("Iniciando predicción...")

            # Validar formato de la imagen
            if "." not in image_file.filename or image_file.filename.split(".")[-1].lower() not in ALLOWED_EXTENSIONS:
                raise ValueError("Formato de imagen no soportado. Solo se permiten PNG, JPG y JPEG.")

            # Validar modelo cargado
            if MODEL is None:
                raise ValueError("El modelo no se ha cargado correctamente.")

            logger.info("Modelo cargado correctamente.")
            start_time = time.time()
            # Preprocesar la imagen
            features = preprocess_imagen(image_file)
            if features is None:
                raise ValueError("Error en el preprocesamiento de la imagen.")

            logger.info("Imagen preprocesada correctamente.")

            # Verificar la forma de `features`
            if len(features.shape) != 2:
                raise ValueError(f"Dimensión incorrecta de las características: {features.shape}")

            # Hacer predicción
            prediction = MODEL.predict(features)[0]

            # Manejar predict_proba si está disponible
            if hasattr(MODEL, "predict_proba"):
                probabilities = MODEL.predict_proba(features)
                confidence = max(probabilities[0])

            processing_time = time.time() - start_time
            
            logger.info(f"Predicción realizada: {prediction} con confianza {confidence:.2f}")

            # Generar un nombre único para la imagen
            image_id = str(uuid.uuid4())
            image_filename = f"{image_id}_{image_file.filename}"
            image_path = f"/uploads/{image_filename}"  

            # Guardar en la base de datos
            with SessionLocal() as db:
                new_prediction = PredictionPostgres(
                    predicted_mineral=str(prediction),
                    confidence=float(round(confidence * 100, 2)),
                    image_name=image_filename,
                    image_path=image_path,
                    source="API",
                    model_version="v1.0",
                    processing_time=float(round(processing_time,2)),
                    feedback=None,
                    real_label=None,
                    user_id=user_id
                )
                db.add(new_prediction)
                db.commit()
                db.refresh(new_prediction)
            logger.info(f"Predicción almacenada en la base de datos con ID {new_prediction.id}")

            return {
                "id": str(new_prediction.id),
                "prediction": prediction,
                "confidence": round(confidence * 100, 2)
            }

        except ValueError as ve:
            logger.warning(f"Error de validación: {str(ve)}")
            return {"error": str(ve)}

        except Exception as e:
            logger.exception("Error inesperado en la predicción")
            return {"error": f"Error inesperado en la predicción: {str(e)}"}

    @staticmethod
    def get_prediction(prediction_id):
        """Obtiene una predicción almacenada en la base de datos por ID."""
        try:
            logger.info(f"Consultando predicción con ID {prediction_id}...")

            with SessionLocal() as db:
                prediction = db.query(PredictionPostgres).filter_by(id=prediction_id).first()

            if prediction:
                logger.info(f"Predicción encontrada: {prediction.predicted_mineral} con confianza {prediction.confidence:.2f}")
                return {
                    "id": prediction.id,
                    "prediction": prediction.predicted_mineral,
                    "confidence": float(round(prediction.confidence, 2)),
                    "image_name": prediction.image_name,
                    "image_path": prediction.image_path,
                    "source": prediction.source,
                    "model_version": prediction.model_version,
                    "feedback": prediction.feedback,
                    "real_label": prediction.real_label
                }

            logger.warning(f"Predicción con ID {prediction_id} no encontrada.")
            return {"error": "Predicción no encontrada"}

        except Exception as e:
            logger.exception("Error inesperado al obtener la predicción")
            return {"error": f"Error al obtener la predicción: {str(e)}"}

    
    @staticmethod
    def correct_prediction(prediction_id, confirmation, correct_mineral=None):
        """Actualiza una predicción basada en la corrección del usuario."""
        try:
            logger.info(f"Procesando corrección para la predicción ID {prediction_id}...")

            with SessionLocal() as db:
                prediction = db.query(PredictionPostgres).filter_by(id=prediction_id).first()

                if not prediction:
                    logger.warning(f"No se encontró la predicción con ID {prediction_id}.")
                    return {"error": "Predicción no encontrada"}

                if confirmation == "si":
                    prediction.feedback = False  # El usuario confirmó que es correcta
                    logger.info(f"Predicción ID {prediction_id} confirmada como correcta.")

                elif confirmation == "no" and correct_mineral:
                    prediction.feedback = True  # El usuario dijo que es incorrecta
                    prediction.real_label = correct_mineral  # Guardamos la corrección
                    logger.info(f"Predicción ID {prediction_id} corregida a {correct_mineral}.")

                db.commit()  # Guardamos los cambios en la base de datos

            return {"message": "Corrección registrada correctamente"}

        except Exception as e:
            logger.exception(f"Error al registrar corrección para la predicción {prediction_id}")
            return {"error": f"Error al registrar corrección: {str(e)}"}