from fastapi import APIRouter
from commons.log import Log


router = APIRouter()


@router.get("/{name}", summary="Hello World", response_model_exclude_unset=True)
async def hello_world(name: str):
    if name:
        Log(f'request funcionando {name}').info()
    return {"message": f"Hello {name}"}
