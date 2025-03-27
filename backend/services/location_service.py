from backend.database.database import SessionLocal
from backend.models.location import LocationPostgreSQL

class LocationService:
    @staticmethod
    def create_location(location_name, user_id):
        """Crea una nueva ubicación en la base de datos"""
        try:
            with SessionLocal() as db:
                new_location = LocationPostgreSQL(name=location_name, user_id=user_id)
                db.add(new_location)
                db.commit()
                db.refresh(new_location)

                return {"message": "Ubicación guardada", "location_id": new_location.id}
        
        except Exception as e:
            return {"error": f"Error al guardar la ubicación: {str(e)}"}
