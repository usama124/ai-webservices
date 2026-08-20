from fastapi import APIRouter
from services import llm_services

router = APIRouter()


@router.post("/generate_story")
async def story_generator(data: dict):
    text = data.get("text", "")
    response = llm_services.generate_story(text)
    return {"output": response}
