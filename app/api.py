from pathlib import Path
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Reasoning AI", version="1.0.0")

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

LLAMA_SERVER_URL = os.getenv("LLAMA_SERVER_URL", "http://127.0.0.1:8080/completion")


SYSTEM_PROMPT = """
You are a reflective assistant engaging in thorough, iterative reasoning,
mimicking human stream-of-consciousness thinking.
Your approach emphasizes exploration, self-doubt,
and continuous refinement before coming up with an answer.

<problem>
{}
</problem>
"""


class PromptRequest(BaseModel):
    prompt: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate")
def generate(data: PromptRequest):

    formatted_prompt = SYSTEM_PROMPT.format(data.prompt)

    payload = {
        "prompt": formatted_prompt,
        "n_predict": 512,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": ["</s>"]
    }

    try:
        response = requests.post(
            LLAMA_SERVER_URL,
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail="Llama server request failed") from exc

    return {
        "input": data.prompt,
        "response": result.get("content", "")
    }