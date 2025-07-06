from elasticsearch import Elasticsearch
import json
import traceback
import pyodbc
from config import SQL_SERVER_CONFIG, ELASTICSEARCH_URL, ELASTICSEARCH_API_KEY

# Conexión a SQL Server
try:
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={SQL_SERVER_CONFIG["server"]};'
        f'DATABASE={SQL_SERVER_CONFIG["database"]};'
        f'UID={SQL_SERVER_CONFIG["username"]};'
        f'PWD={SQL_SERVER_CONFIG["password"]}'
    )
    cursor = conn.cursor()
    print("Conexión a SQL Server exitosa.")
except Exception as e:
    print(f"Error de conexión a SQL Server: {str(e)}")
    traceback.print_exc()  # Imprime la traza completa del error
    exit(1)  # Detener el script si hay un error en la conexión

# Conexión a Elasticsearch utilizando la URL y API Key directamente
try:
    es = Elasticsearch(
        ELASTICSEARCH_URL,  # Usar la URL de Elasticsearch desde el archivo .env
        api_key=ELASTICSEARCH_API_KEY  # Usar la API Key desde el archivo .env
    )
    print("Conexión a Elasticsearch exitosa.")
except Exception as e:
    print(f"Error de conexión a Elasticsearch: {str(e)}")
    traceback.print_exc()  # Imprime la traza completa del error
    exit(1)  # Detener el script si hay un error en la conexión

def fetch_and_send_logs():
    try:
        cursor.execute("SELECT * FROM logs ORDER BY change_time DESC")  # Asegúrate de que esta consulta es correcta
        logs = cursor.fetchall()

        if not logs:
            print("No se encontraron logs en la base de datos.")
            return  # Si no hay logs, salir de la función

        for log in logs:
            log_id = log[0]
            user_id = log[1]
            operation = log[2]
            change_time = log[3]
            old_data = log[4]
            new_data = log[5]

            # Convertir los datos antiguos y nuevos a JSON
            old_data_json = json.loads(old_data) if old_data else None
            new_data_json = json.loads(new_data) if new_data else None

            # Crear documento para Elasticsearch
            doc = {
                "log_id": log_id,
                "user_id": user_id,
                "operation": operation,
                "change_time": change_time,
                "old_data": old_data_json,
                "new_data": new_data_json
            }

            # Indexar documento en Elasticsearch
            es.index(index="logs", document=doc)

        print("Logs procesados y enviados a Elasticsearch.")
    except Exception as e:
        print(f"Error al procesar los logs: {str(e)}")
        traceback.print_exc()  # Imprime la traza completa del error
        exit(1)  # Detener el script si hay un error al procesar los logs

# Ejecutar la función para procesar y enviar los logs
fetch_and_send_logs()

cursor.close()
conn.close()
