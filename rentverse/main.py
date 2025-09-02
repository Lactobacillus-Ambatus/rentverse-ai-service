from fastapi import FastAPI

app = FastAPI(
    title="RentVerse AI Service",
    version="0.1.0",
    description="A FastAPI service for RentVerse AI",
)


@app.get('/')
def read_root():
    return {
        "message": "Welcome to the RentVerse AI Service"
    }
