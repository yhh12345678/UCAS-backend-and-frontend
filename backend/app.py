from flask import Flask, request, jsonify

app = Flask(__name__)




users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# GET 请求示例：返回数据
@app.route('/api/users', methods=['GET'])
def get_users():
    
    return jsonify(users)  # 自动设置 Content-Type: application/json

# POST 请求示例：接收 JSON 并处理
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()  # 解析请求体中的 JSON
    if not data or 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    users.append({"id": 3, "name": data['name']})
    return jsonify(users), 201  # 201 Created

# 带路径参数的 GET 请求
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 模拟从数据库查找
    user = {"id": user_id, "name": "Sample User"}
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)  # debug 模式方便开发，生产环境需关闭