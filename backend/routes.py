from fastapi import APIRouter, HTTPException
from backend.models import Query
from backend.services import add_message

router = APIRouter()

@router.post("/ask")
async def ask_chatbot(query: Query):
    try:
        answer = add_message("user", query.question)
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))