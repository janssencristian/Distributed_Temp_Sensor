from fastapi import FastAPI

app = FastAPI()

@app.post("/aggregate")
async def receive_data(data: dict):
    print(f"Dados agregados recebidos: {data}")
    return {"status": "cloud-ok"}