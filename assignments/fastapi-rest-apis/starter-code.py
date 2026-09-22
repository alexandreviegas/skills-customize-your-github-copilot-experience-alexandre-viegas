from fastapi import FastAPI

app = FastAPI(title="Task API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add your resource model, in-memory storage, and CRUD endpoints here
