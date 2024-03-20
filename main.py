from collections import OrderedDict
from typing import Dict, Optional

from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI()

# Fake database stored in memory
vendas = OrderedDict(
    {
        1: {"id": 1, "nome": "Venda 1", "valor": 100.0},
        2: {"id": 2, "nome": "Venda 2", "valor": 200.0},
        3: {"id": 3, "nome": "Venda 3", "valor": 300.0},
    }
)


@app.get(
    "/"
)  # This is a decorator that tells FastAPI that the function below is a route handler
def home():
    return {"Vendas": len(vendas)}


@app.get("/vendas/{id_venda}")
def get_vendas(id_venda: int):  # we need to inform the type of the parameter
    venda = vendas.get(id_venda)
    if not venda:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venda com id {id_venda} não encontrada",
        )
    return venda


# we can store these models in a separate file and import them
class Venda(BaseModel):
    nome: str
    valor: float
    unidades: Optional[int] = None


@app.post("/vendas/")
def create_vendas(venda: Venda):
    id_venda = len(vendas) + 1
    venda_data = {"id": id_venda}
    venda_data.update(venda.model_dump())
    vendas[id_venda] = venda_data
    return venda_data  # is good practice to return the created object
