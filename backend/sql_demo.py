from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import os
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


#print(f"当前工作目录: {os.getcwd()}")

'''print(f"数据库URI: {app.config['SQLALCHEMY_DATABASE_URI']}")'''


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




with app.app_context():
    db.create_all()  # 创建新表
    email='john@example.com'
    user = User.query.filter_by(email=email).first()
    if user:
         print("用户已存在")
    else:
        new_user = User(username='john', email=email)  # 这是一个实例
        # 将用户对象添加到数据库会话
        db.session.add(new_user)  # 数据库里加入了这个对象
        # 提交会话，保存到数据库
        db.session.commit()
    # 查询所有用户
    all_users = User.query.all()
    print (all_users)
# 根据主键ID查询单个用户
    user_by_id =db.session.get(User, 1)

# 使用过滤器查询，获取第一个匹配的用户

# 使用过滤器查询，获取所有匹配的用户

#users = User.query.filter(User.email.endswith('@example.com')).all()
    print(user_by_id)


    #数据删除过程

    user = User.query.get(1)
    # 标记要删除的对象
    db.session.delete(user)
    # 提交会话，执行删除
    db.session.commit()
    '''
    # 查询ID为1的用户
    user_1 = db.session.get(User, 1)
    # 修改其用户名
    user.username = 'johndoe'
    # 提交会话，保存更改
    db.session.commit()

'''

# 创建一个新用户










