from fastapi import FastAPI
import models 
from config import engine 
from routes import router

#models.Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def home():
    return "Welcome"

app.include_router(router, prefix="/persona", tags=["persona"])