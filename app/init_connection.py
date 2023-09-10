import mysql.connector
import os


# Configuração das informações de conexão (substitua pelos seus próprios dados)
db_config = {
    "host": os.environ.get("DB_HOST"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_DATABASE"),
}
