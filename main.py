from fastapi import FastAPI 

app = FastAPI(
    title="API de Cálculos",
    description="API desenvolvida na oficina do IFSC",
    version="1.0.0"
)

@app.get("/{nome}")
def home(nome: str):
    return {
        "mensagem": f"Olá {nome}"
    }

from pydantic import BaseModel, Field

class DadoIMC(BaseModel):
    peso: float = Field(gt=0)
    altura: float = Field(gt=0)

@app.post("/imc")
def calcular_imc(dados: DadoIMC):
    resultado = dados.peso / (dados.altura ** 2)

    return {
        "imc": round(resultado,2)
    }
