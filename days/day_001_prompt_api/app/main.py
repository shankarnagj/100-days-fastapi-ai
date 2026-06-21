from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="Day 1 Prompt API",
    description="100 Days of FastAPI for AI Engineering",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def home():
    return{
        "message": "Welcome to Day 1 Prompt API"
    }