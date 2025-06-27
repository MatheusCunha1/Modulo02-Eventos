from fastapi import APIRouter
from app.database import create_evento, get_eventos, update_evento, delete_evento
from app.models import Evento

router = APIRouter()

@router.post("/eventos/")
async def create(evento: Evento):
    return await create_evento(evento)

@router.get("/eventos/")
async def read():
    return await get_eventos()

@router.put("/eventos/{evento_id}")
async def update(evento_id: str, evento: Evento):
    return await update_evento(evento_id, evento)

@router.delete("/eventos/{evento_id}")
async def delete(evento_id: str):
    return await delete_evento(evento_id)
