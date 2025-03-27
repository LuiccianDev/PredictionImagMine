from backend.app import create_app
from backend.config import PORT, DEBUG, HOST

app = create_app()

if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG, host=HOST)