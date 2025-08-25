from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API funcionando en Render 🚀"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}
