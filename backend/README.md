# app.py中是简单的flask提供API

## 可用如下代码实现调用（powershell代码）：

### GET 所有用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users

### POST 创建用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users `-Method Post `-ContentType "application/json" `-Body '{"name":"Charlie"}'

### GET 单个用户
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/users/123