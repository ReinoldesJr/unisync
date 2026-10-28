from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Motor de Oportunidades (protótipo)")

# Libera o Shell (Django) e o feed (Vite) a chamarem esta API pelo navegador
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173", "http://127.0.0.1:5173",
        "http://localhost:8000", "http://127.0.0.1:8000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

OPPORTUNITIES = [
    {"id": "1", "title": "Palestra: Carreira em Dados", "type": "palestra",
     "description": "Bate-papo com profissionais da área de dados.", "deadline": "2026-11-10"},
    {"id": "2", "title": "Estágio em Desenvolvimento Web", "type": "estagio",
     "description": "Vaga para estudantes de Computação, 6h diárias.", "deadline": "2026-11-20"},
    {"id": "3", "title": "Hackathon UNINASSAU", "type": "evento",
     "description": "48 horas para construir soluções para o campus.", "deadline": "2026-12-01"},
    {"id": "4", "title": "Projeto de Extensão: Software Factory", "type": "projeto",
     "description": "Ensino de engenharia de software para escolas públicas.", "deadline": "2026-11-30"},
]


@app.get("/opportunities")
def list_opportunities(q: Optional[str] = None, type: Optional[str] = None):
    items = OPPORTUNITIES
    if type:
        items = [o for o in items if o["type"] == type]
    if q:
        term = q.lower()
        items = [o for o in items
                 if term in o["title"].lower() or term in o["description"].lower()]
    return items