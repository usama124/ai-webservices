from fastapi import FastAPI, APIRouter, Depends

from fastapi.middleware.cors import CORSMiddleware
from auth import verify_api_key
from routers import chatbot, summarize, story_generator, code_explainer, grammer_polisher, lang_translator

app = FastAPI(
    title="AI Webservices",
    description="API for AI Webservices",
    version="1.0.0"
)

# Enable CORS so your Bluehost site can communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with "https://yourdomain.com" in production
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(dependencies=[Depends(verify_api_key)])
api_router.include_router(chatbot.router, prefix="/api/v1")
api_router.include_router(summarize.router, prefix="/api/v1")
api_router.include_router(code_explainer.router, prefix="/api/v1")
api_router.include_router(story_generator.router, prefix="/api/v1")
api_router.include_router(grammer_polisher.router, prefix="/api/v1")
api_router.include_router(lang_translator.router, prefix="/api/v1")

app.include_router(api_router)
