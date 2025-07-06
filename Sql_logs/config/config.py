from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración de SQL Server
SQL_SERVER_CONFIG = {
    'server': os.getenv('SQL_SERVER_HOST'),
    'database': os.getenv('SQL_SERVER_DB'),
    'username': os.getenv('SQL_SERVER_USER'),
    'password': os.getenv('SQL_SERVER_PASSWORD'),
}

# Configuración de Elasticsearch
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
ELASTICSEARCH_API_KEY = os.getenv("ELASTICSEARCH_API_KEY")
