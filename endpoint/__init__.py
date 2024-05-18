from fastapi import FastAPI
from . import hello


app = FastAPI()

app.include_router(hello.router, prefix="/hello", tags=["hello"])