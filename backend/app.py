from flask import Flask, request, jsonify
import requests
import ollama
import json

from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'chat.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 10,          # 连接池的大小
    'pool_recycle': 3600,     # 连接回收时间（秒），避免MySQL 8小时断开连接的问题
    'pool_pre_ping': True,    # 每次使用连接前检查其是否有效
    'pool_timeout': 30,       # 从池中获取连接的超时时间（秒）
    'max_overflow': 20,       # 连接池允许的最大溢出连接数
}
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()






conversation_history = []#保持记忆

@app.route('/')
def hello():
    return "<p>welcome to our LLM</p>"

#单轮对话，无记忆
'''
@app.route('/api/qwen',methods=['POST'])
def test_qwen_api():

    data=request.get_json()
    model=data['model']
    messages = data['prompt']
    response = ollama.generate(model=model, prompt=messages)
    #messages.append(response['message'])
    return jsonify({'content': response['response']})
'''


#多轮对话
@app.route('/api/qwen',methods=['POST'])
def test_qwen_api():

    data=request.get_json()#data此时是字典类型
    model=data['model']
    messages = data.get('messages')
    conversation_history.append({"role": "user", "content":messages[-1]['content']})
    response = ollama.chat(model=model, messages=conversation_history)
    conversation_history.append({'role':"assistant",'content':response['message']['content']})
    return jsonify({'role':"assistant",'content': response['message']['content']})



# 带路径参数的 GET 请求
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 模拟从数据库查找
    user = {"id": user_id, "name": "Sample User"}
    return jsonify(user)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # debug 模式方便开发，生产环境需关闭