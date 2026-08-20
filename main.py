from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from routers import chatbot, summarize

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

api_router = APIRouter()
api_router.include_router(chatbot.router, prefix="/api/v1")
api_router.include_router(summarize.router, prefix="/api/v1")
