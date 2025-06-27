from pydantic import BaseModel

class EventoSchema(BaseModel):
    titulo: str
    descricao: str
    data: str
    local: str
