from app.models import Evento
from app.schema import EventoSchema

# Simulação de banco de dados em memória
eventos_db = []


def get_eventos(evento_id=None):
    if evento_id is None:
        return eventos_db
    return eventos_db[evento_id] if evento_id < len(eventos_db) else None

def create_evento(evento: EventoSchema):
    evento_obj = Evento(**evento.dict())
    eventos_db.append(evento_obj)
    return evento_obj

def update_evento(evento_id: int, evento: EventoSchema):
    if evento_id < len(eventos_db):
        eventos_db[evento_id] = Evento(**evento.dict())
        return eventos_db[evento_id]
    return None

def delete_evento(evento_id: int):
    if evento_id < len(eventos_db):
        return eventos_db.pop(evento_id)
    return None
