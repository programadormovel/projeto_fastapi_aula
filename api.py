import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/exemplo")
def example() -> str:
    return "Olá Mundo"

if __name__ == "__main__":
    print(example())
    uvicorn.run(app, port=8087)


