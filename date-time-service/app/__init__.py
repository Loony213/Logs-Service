from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')  # Cargar configuración

    # Importar las rutas
    from .routes import date_time_blueprint
    app.register_blueprint(date_time_blueprint)

    return app
