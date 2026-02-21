import requests
import random
import time
import os

EDGE_URL = os.environ.get("EDGE_URL")

while True:
    temperature = random.uniform(60, 100)

    data = {
        "sensor_id": "sensor-1",
        "temperature": temperature
    }

    try:
        requests.post(f"{EDGE_URL}/temperature", json=data, timeout=1)
        print(f"Enviado: {temperature}")
    except:
        print("Falha ao enviar")

    time.sleep(1)