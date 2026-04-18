from flask import Flask, request, jsonify
import requests
import ollama
import json
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



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

#创建数据库实例
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)











    #创建数据库中的一张表
class Model(db.Model,):  # 继承父类
            # 定义列
            id = db.Column(db.Integer, primary_key=True)    # 主键，自增整数
            role = db.Column(db.String(80), unique=False, nullable=False)# 用户名，唯一，不可为空
            content = db.Column(db.String(80), unique=False, nullable=False)
            # 可以继续添加其他字段
            @classmethod
            def add_instance(cls,role_1, content):
                new_user_1 = cls(role=role_1, content=content)
                # 这是一个实例
                # 将用户对象添加到数据库会话
                db.session.add(new_user_1)
                # 数据库里加入了这个对象
                # 提交会话，保存到数据库
                db.session.commit()


            def to_dict(self):
                return {
                    'id': self.id,
                    'role': self.role,
                    'content': self.content
                }

            def __repr__(self):
                return f'<User id={self.id} role={self.role} content={self.content}>'





with app.app_context():
    db.create_all()
    #db.session.query(Model).delete()
    #db.session.commit()# 创建新表
    all_users = Model.query.all()
    print (all_users)



    #数据删除过程
#    db.session.query(Model).delete()
 #   db.session.commit()











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

    Model.add_instance("user", messages[-1]['content'])

    conversation_history = [user.to_dict() for user in Model.query.all()]

    response = ollama.chat(model=model, messages=conversation_history)

    Model.add_instance("assistant", response['message']['content'])

    return jsonify({'role':"assistant",'content': response['message']['content']})



# 带路径参数的 GET 请求
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # 模拟从数据库查找
    user = {"id": user_id, "name": "Sample User"}
    return jsonify(user)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # debug 模式方便开发，生产环境需关闭