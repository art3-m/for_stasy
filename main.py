from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# CORS (чтобы фронт спокойно стучался)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# простая "база"
db = []

class Answer(BaseModel):
    choice: str

@app.post("/answer")
def answer(data: Answer):
    db.append({
        "choice": data.choice,
        "time": datetime.now().isoformat()
    })
    return {"status": "ok"}

@app.get("/results")
def results():
    return db

# 🔥 ВАЖНО: раздача фронта
app.mount(
    "/for_stasy",
    StaticFiles(directory="/", html=True),
    name="for_stasy"
)
