from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, World"}


@app.get("/saudacao")
async def saudacao(string: str):
    return {"message": "Olá, {string}! seja bem-vindo!"}