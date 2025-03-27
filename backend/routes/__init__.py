
from .prediction_route import prediction_bp
from .auth_route import auth_bp
from .user_route import user_bp
from .device_route import device_bp
from .label_route import label_bp
from .location_route import location_bp

def register_blueprints(app):
    app.register_blueprint(prediction_bp, url_prefix="/api/predictions")
    app.register_blueprint(auth_bp, url_prefix="/api/auths")
    app.register_blueprint(user_bp, url_prefix="/api/user/profile")
    app.register_blueprint(device_bp, url_prefix="/api/devices")
    app.register_blueprint(label_bp, url_prefix="/api/labels")
    app.register_blueprint(location_bp, url_prefix="/api/locations")