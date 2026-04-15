# app.py中是简单的flask提供API

## 可用如下代码实现调用（powershell代码）：

### GET 所有用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users

### POST 创建用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users `-Method Post `-ContentType "application/json" `-Body '{"name":"Charlie"}'

### GET 单个用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users/123

### @app.route('/proxy/mediastack', methods=['GET'])的使用
    注册mediastack账号（https://mediastack.com/），在Dashboard一栏找到your api key 复制并替换url一栏中的括号部分，即可进行API调用