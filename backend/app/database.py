import motor.motor_asyncio
from app.models import Evento
from typing import List
from bson import ObjectId 

# URI de conexão com o MongoDB
MONGO_URI = "mongodb://db-eventos:27017"

# Nome do banco de dados
DB_NAME = "eventos_db"

# Criação do cliente MongoDB (motor)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

# Criação do banco de dados
db = client[DB_NAME]

# Definindo a coleção "eventos"
eventos_collection = db["eventos"]

# Função para criar evento
async def create_evento(evento: Evento):
    evento_dict = evento.dict()
    result = await eventos_collection.insert_one(evento_dict)
    return str(result.inserted_id)

# Função para obter todos os eventos
async def get_eventos():
    eventos_cursor = eventos_collection.find()
    eventos = await eventos_cursor.to_list(length=100)
    
    for evento in eventos:
        evento["_id"] = str(evento["_id"])  # Convertendo o ObjectId para string
    
    return eventos

# Função para atualizar evento
async def update_evento(evento_id: str, evento: Evento):
    try:
        # Convertendo o evento_id para ObjectId
        evento_object_id = ObjectId(evento_id)
        
        evento_dict = evento.dict()
        result = await eventos_collection.update_one(
            {"_id": evento_object_id}, {"$set": evento_dict}
        )
        
        if result.modified_count > 0:
            return {"message": "Evento atualizado com sucesso."}
        else:
            return {"message": "Evento não encontrado ou não houve alterações."}
    
    except Exception as e:
        return {"error": f"Erro na atualização: {str(e)}"}

async def delete_evento(evento_id: str):
    try:
        # Tentando converter o ID para ObjectId
        evento_object_id = ObjectId(evento_id)
        result = await eventos_collection.delete_one({"_id": evento_object_id})
        
        # Verifica se a exclusão foi bem-sucedida
        if result.deleted_count > 0:
            return {"message": "Evento excluído com sucesso."}
        else:
            return {"message": "Evento não encontrado."}
    
    except Exception as e:
        # Se houver erro de conversão
        return {"error": f"Erro na exclusão: {str(e)}"}

# Teste de conexão
async def test_connection():
    try:
        # Tenta acessar as coleções do banco
        collections = await db.list_collection_names()
        return {"collections": collections}
    except Exception as e:
        return {"error": str(e)}
