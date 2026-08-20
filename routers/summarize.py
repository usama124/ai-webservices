from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/summarize")
async def chat(data: dict):
    text = data.get("text", "")
    response = llm_services.summarize(text)
    return {"output": response}
