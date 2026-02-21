from fastapi import FastAPI
import requests
import os
import time

app = FastAPI()

CLOUD_URL = os.environ.get("CLOUD_URL")

total_messages = 0
alert_count = 0

@app.post("/temperature")
async def receive_temperature(data: dict):
    global total_messages, alert_count
    total_messages += 1

    temperature = data["temperature"]

    if temperature > 80:
        alert_count += 1
        print(f"ALERTA LOCAL! Temperatura crítica: {temperature}")

    if total_messages % 10 == 0:
        try:
            requests.post(f"{CLOUD_URL}/aggregate", json={
                "total": total_messages,
                "alerts": alert_count
            })
        except:
            print("Cloud indisponível")

    return {"status": "ok"}