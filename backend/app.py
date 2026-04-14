from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

# app.route()的常见用法



@app.route('/')
def index():
    return f'Index Page {url_for('index')}'

#@app.route('/hello')

#def hello_world():
#    return f"<p>Hello, World!</p> {url_for('hello_world')}"

#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#加入post方法的login界面

#@app.route('/login',methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        return do_the_login()
#   else:
#        return show_the_login_form()

###
#上方代码的另一种表达
#@app.get('/login')
#def login_get():
#    return show_the_login_form()

#@app.post('/login')
#def login_post():
#    return do_the_login()

####

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

#with app.test_request_context():
#    print(url_for('index'))
#    print(url_for('login'))
#    print(url_for('login', next='/'))
#    print(url_for('profile', username='John Doe'))

###
#生成静态文件的 URL，请使用特殊的 'static' 端点名称
#url_for('static', filename='style.css')

###
#模板渲染
#Flask 会在 templates 文件夹中查找模板。如果你的应用是一个模块，那么这个文件夹就位于模块旁边；如果你的应用是一个包，那么它实际上位于包内部
#在模板内部，您还可以访问 config, request, session 和 g [1] 对象以及:func:~flask.url_for 和 get_flashed_messages() 函数。
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


###
#有关method和form属性的用法实例
#@app.route('/login', methods=['POST', 'GET'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
#    # the code below is executed if the request method
#    # was GET or the credentials were invalid
#    return render_template('login.html', error=error)
if __name__ == '__main__':
   app.run(debug=True)