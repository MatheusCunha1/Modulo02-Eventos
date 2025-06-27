from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.eventos import router as eventos_router
from app.database import test_connection
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Eventos! Comunicação Sucedida!"}

@app.get("/test_connection")
async def connection_test():
    return await test_connection()

app.include_router(eventos_router)
