import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

# Obtener variables de entorno
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")
mongo_db = os.getenv("MONGO_DB")

try:
    # Conectar a la base de datos de MongoDB
    client = MongoClient(mongo_host, int(mongo_port))
    db = client[mongo_db]
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
