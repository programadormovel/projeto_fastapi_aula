import uvicorn, json
from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware

from pessoa import Pessoa
from pessoa_operations import PessoaOperations
from commons.routes import API_DOC_JSON, API_DOC_REDOC, API_DOC, API_HEALTH, API_READINESS, URL_PREFIX
from endpoint import app as endpoints
# from config import DEBUG
#from healthcheck import HealthCheck

app = FastAPI(title="aplicacao teste do treinamento",
              description="api teste",
              docs_url=API_DOC,
              openapi_url=API_DOC_JSON,
              redoc_url=API_DOC_REDOC,
              debug=True)

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_headers=["*"],
                   allow_credentials=True,
                   allow_methods=["*"])

#app.add_api_route(API_HEALTH, lambda: HealthCheck(status='OK'), summary='Health check', tags=['info'])

#app.add_api_route(API_READINESS, lambda: hc(HealthCheck), summary="Health check")


def hc(response: Response):
    message, status_code, headers = HealthCheck().run_check()
    response.status_code = status_code
    response.headers = headers
    message = (json.loads(message))
    status = {key: message[key] for key in ['status'] if key in message}
    return status

app.include_router(endpoints.router, prefix=URL_PREFIX)

@app.get("/exemplo")
def example() -> dict:
    a = 5
    b = 2

    return { 'exemplo' : "Olá Mundo" + str(a+b)}

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

#if __name__ == "__main__":
#    uvicorn.run("api:app", port=8087, workers=1, reload=True)




