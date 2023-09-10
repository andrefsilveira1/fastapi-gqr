from fastapi import FastAPI, APIRouter, File, UploadFile, HTTPException
import pandas as pd
import io
import mysql.connector
from init_connection import db_config

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/test")
async def test_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        conn.close()
        return {"message": "Conexão com o MySQL bem-sucedida!"}
    except Exception as e:
        return {"message": f"Erro ao conectar ao MySQL: {str(e)}"}

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}

@api_router.post("/file", status_code=200)
async def create_upload_file(file: UploadFile = File(...)):
    """
    Root POST
    """
    try:
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=422, detail="O arquivo enviado não é um arquivo CSV.")

        csv_content = await file.read()
        df = pd.read_csv(io.StringIO(csv_content.decode("utf-8"))).head()
        
        return {"file_data": df.to_dict(orient="records")}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo CSV: {str(e)}")

@api_router.post("/exportar/csv/{name}", status_code=200)
def export_csv(*, name: str) -> dict:
    """
    Root POST
    """
    query = name
    return {"msg": f"File Downloaded: {name}"}
@api_router.get("/exportar/csv/{name}", status_code=200)
def get_export_csv(*, name: str) -> dict:
    """
    Root GET
    """
    query = name
    return {"msg": f"File Downloaded with GET: {query}"}


@api_router.get("/submissoes", status_code=200)
def get_submissions() -> dict:
    """
    Root GET
    """
    return {"msg": "Submissions requested"}

@api_router.get("/gqr/{id}", status_code=200)
def get_gqr_id(*, id: int) -> dict:
    """
    Root GET
    """
    result = id
    return {"msg": f"GQR requested: {result}"}

@api_router.get("/submissoes/{id}", status_code=200)
def get_submissions_id(*, id: int) -> dict:
    """
    Root GET
    """
    query = id
    return {"msg": f"Submissions id requested: {query}"}

@api_router.delete("/submissoes/{id}", status_code=200)
def delete_submissions(*, id: int) -> dict:
    """
    Root DELETE
    """
    query = id
    return {"msg": f"Submissions id requested {query}"}

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")