from app.routes import app
from waitress import serve
from app.config import Config

if __name__ == '__main__':
    host = Config.host
    port = Config.port
    print(f"Serving on http://{host}:{port}")
    serve(app, host=host, port=port)
