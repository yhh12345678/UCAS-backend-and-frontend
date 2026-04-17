from flask import Flask, request, jsonify
import requests
import json
app = Flask(__name__)


@app.route('/')
def hello():
    return "<p>hello world</p>"


#提供API为客户端调用
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# GET 请求示例：返回数据
@app.route('/api/users', methods=['GET'])
def get_users():
    
    return jsonify(users)  # 自动设置 Content-Type: application/json


# POST 请求示例：接收 JSON 并处理
@app.route('/api/users', methods=['POST'])
def create_user():

    data = request.get_json()
    
    
      # 解析请求体中的 JSON
    if not data or 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    users.append({"id": 3, "name": data['name']})
    return jsonify(users), 201  # 201 Created


@app.route('/api/qwen',methods=['POST'])
def test_qwen_api():

    data=request.get_json()

    response = requests.post(
      "http://localhost:11434/api/chat",
      json=data        
  )

    return jsonify(response.json()["message"])
    


# 带路径参数的 GET 请求
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 模拟从数据库查找
    user = {"id": user_id, "name": "Sample User"}
    return jsonify(user)


#调用外部的API
@app.route('/proxy/mediastack', methods=['GET'])
def call_mediastack_api():
    # 调用 GitHub 公开 API
    url = 'https://api.mediastack.com/v1/news?access_key=()&keywords=war&countries=cn'
    try:
        response = requests.get(url, timeout=5)
        #response = requests.get(url, timeout=5)  # 设置超时，避免阻塞
        response.raise_for_status()              # 如果状态码不是 200，抛出异常
        data = response.json()                   # 解析返回的 JSON
        return data['data'],200
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # debug 模式方便开发，生产环境需关闭