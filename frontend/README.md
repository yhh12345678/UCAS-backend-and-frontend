使用streamlit在网页上运行，要接ollama，不然没有输出

用streamlit构建前端，接入flask提供的API

# requirements( 需要的库)
flask
streamlit
requests
request
jsonify
time

	可用 pip install 进行安装


#在本地使用时要修改backend_URL的值

		backend_URL="(此处填写运行flask时弹出的第一个IP地址)/api/qwen"
		
#运行顺序 

	先运行flask后端服务器
		cd .\backend
		python app.py
	再运行前端网页
		cd ..
		cd .\frontend
		streamlit run "app v1.1.py"
	