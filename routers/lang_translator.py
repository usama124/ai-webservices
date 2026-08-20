from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/lang_translator")
async def language_translator(data: dict):
    text = data.get("text", "")
    response = llm_services.translate_text(text)
    return {"output": response}
