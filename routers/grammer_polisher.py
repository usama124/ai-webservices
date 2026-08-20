from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/polish-grammer")
async def grammer_polisher(data: dict):
    text = data.get("text", "")
    response = llm_services.polish_text(text)
    return {"output": response}
