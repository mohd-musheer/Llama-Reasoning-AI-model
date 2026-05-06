from pathlib import Path
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import httpx
from fastapi.middleware.cors import CORSMiddleware 

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Reasoning AI", version="1.0.0")

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

app.add_middleware(
    
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

LLAMA_SERVER_URL = os.getenv(
    "LLAMA_SERVER_URL",
    "http://127.0.0.1:8080/v1/chat/completions"
)

SYSTEM_PROMPT = """
You are a reflective assistant engaging in thorough reasoning.

<problem>
{}
</problem>
"""

class PromptRequest(BaseModel):
    prompt: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/generate")
async def generate(data: PromptRequest):

    formatted_prompt = SYSTEM_PROMPT.format(data.prompt)

    payload = {
        "messages": [
            {
                "role": "user",
                "content": formatted_prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }

    try:
        async with httpx.AsyncClient(timeout=300.0) as client:

            response = await client.post(
                LLAMA_SERVER_URL,
                json=payload
            )

            response.raise_for_status()

            result = response.json()

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Llama server connection failed: {str(exc)}"
        )

    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Llama server error: {exc.response.text}"
        )

    return {
        "input": data.prompt,
        "response": result["choices"][0]["message"]["content"]
    }
    
    