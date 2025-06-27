# 🗓️ Gestão de Eventos

Sistema simples de gerenciamento de eventos desenvolvido com **Python**, **FastAPI**, **MongoDB**, e **HTML/CSS/JS puro**.

---

## 🚀 Tecnologias Utilizadas

- **Backend:** Python + FastAPI  
- **Banco de Dados:** MongoDB  
- **Frontend:** HTML + CSS + JavaScript puro

---

## 📌 Endpoints Disponíveis

| Método | URL            | Descrição                     |
|--------|----------------|-------------------------------|
| GET    | `/events`      | Lista todos os eventos        |
| GET    | `/events/{id}` | Consulta evento por ID        |
| POST   | `/events`      | Cria um novo evento           |
| PUT    | `/events/{id}` | Atualiza um evento existente  |
| DELETE | `/events/{id}` | Remove um evento              |

---

## 📝 Parâmetros de Entrada

### ➕ Criar Evento (`POST /events`)

```json
{
  "titulo": "Nome do Evento",
  "descricao": "Descrição do evento",
  "data": "2025-06-30T10:00:00Z",
  "local": "Local do evento"
}
````

### ✏️ Atualizar Evento (`PUT /events/{id}`)

Todos os campos são opcionais:

```json
{
  "titulo": "Novo nome do evento",
  "descricao": "Nova descrição",
  "data": "2025-07-01T14:00:00Z",
  "local": "Novo local"
}
```

---

## 📡 Respostas Esperadas

| Código | Descrição                  | Exemplo de Resposta                                |
| ------ | -------------------------- | -------------------------------------------------- |
| 200    | Sucesso (GET, PUT, DELETE) | `{ "message": "Evento atualizado com sucesso" }`   |
| 201    | Criado com sucesso (POST)  | `{ "id": "123abc", "message": "Evento criado" }`   |
| 400    | Requisição inválida        | `{ "error": "Campo 'titulo' é obrigatório" }`      |
| 404    | Evento não encontrado      | `{ "error": "Evento não encontrado" }`             |
| 500    | Erro interno do servidor   | `{ "error": "Erro no servidor, tente novamente" }` |

---

## 📬 Exemplo de Requisição

### Criar Evento (POST `/events`)

**Request:**

```http
POST /events
Content-Type: application/json
```

```json
{
  "titulo": "Workshop de Python",
  "descricao": "Aprenda o básico de Python",
  "data": "2025-06-30T10:00:00Z",
  "local": "Sala 101"
}
```

**Response:**

```json
{
  "id": "abc123xyz",
  "messagem": "Evento criado"
}
```

---

## 📦 Como Executar

```bash
git clone https://github.com/MatheusCunha1/Modulo02-Eventos.git
cd Modulo02-Eventos
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

📣 Projeto acadêmico para a disciplina de Tecnologia Em Desenvolvimento De Sistemas	
Feito por [Matheus Cunha](https://github.com/MatheusCunha1)

```
