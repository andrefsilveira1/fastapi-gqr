from fastapi import FastAPI, APIRouter


app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}

@api_router.post("/upload-csv", status_code=200)
def root() -> dict:
    """
    Root POST
    """
    return {"msg": "File uploaded"}

@api_router.post("/exportar/csv/{name}", status_code=200)
def root() -> dict:
    """
    Root POST
    """
    return {"msg": "File Downloaded"}
@api_router.get("/exportar/csv/{name}", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "File Downloaded with GET"}


@api_router.get("/submissoes", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Submissions requested"}

@api_router.get("/gqr/{id}", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "GQR requested"}

@api_router.get("/submissoes/{id}", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Submissions id requested"}

@api_router.delete("/submissoes/{id}", status_code=200)
def root() -> dict:
    """
    Root DELETE
    """
    return {"msg": "Submissions id requested"}

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")