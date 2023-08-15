from app.routes import app
from waitress import serve

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 1102
    print(f"Serving on http://{host}:{port}")
    serve(app, host=host, port=port)
