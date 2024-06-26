import uvicorn
from fastapi import FastAPI
from pessoa import Pessoa
from pessoa_operations import PessoaOperations

app = FastAPI()
# teste comentario
@app.get("/exemplo")
def example() -> str:
    return "Olá Mundo"

@app.post("/exemplo_2")
def example2(pessoa: Pessoa) -> str:
    # inserção no banco destes dados
    return pessoa.codigo

@app.get("/pegar_pessoa_por_nome")
async def get_nome_pessoa(nome: str) -> dict:
    return await PessoaOperations.get_nome_pessoa(nome)

@app.post("/inserir_pessoa")
async def inserir_pessoa(pessoa: Pessoa) -> str:
    return await PessoaOperations.inserir_pessoa(pessoa)

if __name__ == "__main__":
    uvicorn.run("api:app", port=8087, workers=1, reload=True)




