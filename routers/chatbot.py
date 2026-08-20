from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/chat")
async def chat(data: dict):
    text = data.get("text", "")
    response = llm_services.chat(text)
    return {"output": response}
