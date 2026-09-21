from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 

app = FastAPI() 

### Configura a pasta onde vão ficar os arquivos HTML do front-end

templates = Jinja2Templates(directory="templates") 

TRENOS = {
"peito_triceps": {
"nome": "Treino A - Peito e Tríceps",
"exercicios": [
{"nome": "Supino Reto com Barra", "series": "4x10", "descanso": "60s"},
{"nome": "Supino Inclinado com Halteres", "series": "3x12", "descanso": "60s"},
{"nome": "Crucifixo Máquina (Pec Deck)", "series": "3x12", "descanso": "45s"},
{"nome": "Tríceps Pulley (Corda)", "series": "4x12", "descanso": "45s"},
{"nome": "Tríceps Testa", "series": "3x10", "descanso": "60s"}
]
},
"costas_biceps": {
"nome": "Treino B - Costas e Bíceps",
"exercicios": [
{"nome": "Puxada Alta na Polia", "series": "4x10", "descanso": "60s"},
{"nome": "Remada Baixa Sentada", "series": "3x12", "descanso": "60s"},
{"nome": "Pull-Down com Barra", "series": "3x15", "descanso": "45s"},
{"nome": "Rosca Direta com Barra W", "series": "4x10", "descanso": "60s"},
{"nome": "Rosca Martelo com Halteres", "series": "3x12", "descanso": "45s"}
]
},
"pernas_ombros": {
"nome": "Treino C - Pernas e Ombros",
"exercicios": [
{"nome": "Agachamento Livre", "series": "4x10", "descanso": "90s"},
{"nome": "Leg Press 45°", "series": "4x12", "descanso": "60s"},
{"nome": "Cadeira Extensora", "series": "3x15", "descanso": "45s"},
{"nome": "Desenvolvimento com Halteres", "series": "4x10", "descanso": "60s"},
{"nome": "Elevação Lateral na Polia ou Halter", "series": "4x12", "descanso": "45s"}
]
}
} 

@app.get("/", response_class=HTMLResponse)
async def home(request: Request): 

### Envia os treinos para o arquivo index.html do front-end

return templates.TemplateResponse("index.html", {"request": request, "treinos": TRENOS})
