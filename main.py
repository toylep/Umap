from fastapi import FastAPI
from config.routers import base_router

app = FastAPI()
app.include_router(base_router)
