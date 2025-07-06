from flask import Flask, jsonify
from flask_cors import CORS  # Importar CORS
import subprocess

app = Flask(__name__)

# Habilitar CORS para todas las rutas y todos los orígenes
CORS(app)

@app.route('/load_logs', methods=['POST'])
def load_logs():
    try:
        # Ejecutar el script logs_processor.py cuando se hace una solicitud POST
        subprocess.run(['python', 'logs/logs_processor.py'], check=True)
        return jsonify({"message": "Logs cargados exitosamente en Elasticsearch!"})
    except subprocess.CalledProcessError as e:
        return jsonify({"message": f"Error al cargar los logs: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
