import requests
import json

while True:
    user_input = input("请输入问题（输入 'exit' 退出）：")
    if user_input.lower() == 'exit':
        break

    data = {
        "model": "qwen3.5:0.8b",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "stream": False  
    }

    response = requests.post(
        "http://localhost:11434/api/chat",
        json=data        
    )

    if response.status_code == 200:
        print("AI 回复：", response.json()["message"]["content"])
    else:
        print("请求失败，状态码：", response.status_code)




data = {
  "model": "qwen3.5:0.8b",
  "messages": [
    {
      "role": "user",
      "content": "今天吃什么"
    }
  ],
  "stream": False  
}


response = requests.post(
      "http://localhost:11434/api/chat",
      json=data        
  )


print(response.status_code)
print(response.json()["message"]["content"])   