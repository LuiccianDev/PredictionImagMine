from backend.database.database import SessionLocal
from backend.models.label import LabelPostgres

class LabelService:
    @staticmethod
    def create_label(label_name, prediction_id, user_id):
        """Crea una nueva etiqueta en la base de datos"""
        try:
            with SessionLocal() as db:
                new_label = LabelPostgres(name=label_name, prediction_id=prediction_id, user_id=user_id)
                db.add(new_label)
                db.commit()
                db.refresh(new_label)

                return {"message": "Etiqueta guardada", "label_id": new_label.id}
        
        except Exception as e:
            return {"error": f"Error al guardar la etiqueta: {str(e)}"}
