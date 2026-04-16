import requests
import json


data = {
    "model": "qwen3.5:0.8b",
    "prompt": "hello",
    "stream": False
}


response = requests.post(
    "http://localhost:11434/api/generate",
    json=data          
)


print(response.status_code)
print(response.json()["response"])   