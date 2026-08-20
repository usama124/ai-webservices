from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/code_explainer")
async def code_explainer(data: dict):
    text = data.get("text", "")
    response = llm_services.explain_code(text)
    return {"output": response}
