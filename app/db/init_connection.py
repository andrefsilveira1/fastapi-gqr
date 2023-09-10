import mysql.connector
from fastapi import FastAPI

app = FastAPI()

# Configuração das informações de conexão (substitua pelos seus próprios dados)
db_config = {
    "host": "localhost",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "seu_banco_de_dados"
}

# Cria uma conexão com o banco de dados
conn = mysql.connector.connect(**db_config)

# Rota para testar a conexão
@app.get("/")
async def test_db_connection():
    if conn.is_connected():
        return {"message": "Conexão com o MySQL bem-sucedida!"}
    else:
        return {"message": "Não foi possível conectar ao MySQL."}

# Rota para fechar a conexão
@app.on_event("shutdown")
async def shutdown_db_connection():
    if conn.is_connected():
        conn.close()

# Exemplo de rota para executar uma consulta SQL
@app.get("/fetch-data")
async def fetch_data():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sua_tabela")
    result = cursor.fetchall()
    cursor.close()
    return {"data": result}
