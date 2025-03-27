from backend.database.database import SessionLocal
from backend.models.device import DevicePostgreSQL

class DeviceService:
    @staticmethod
    def create_device(device_name, user_id):
        """Crea un nuevo dispositivo en la base de datos"""
        try:
            with SessionLocal() as db:
                new_device = DevicePostgreSQL(name=device_name, user_id=user_id)
                db.add(new_device)
                db.commit()
                db.refresh(new_device)

                return {"message": "Dispositivo guardado", "device_id": new_device.id}
        
        except Exception as e:
            return {"error": f"Error al guardar el dispositivo: {str(e)}"}
