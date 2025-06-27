from pydantic import BaseModel
from typing import Optional

# Modelo de Evento para o MongoDB
class Evento(BaseModel):
    titulo: str
    descricao: str
    data: str
    local: str

    class Config:
        # Para usar ObjectId no Pydantic
        json_encoders = {
            str: str
        }
