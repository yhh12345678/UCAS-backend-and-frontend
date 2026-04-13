后端软件flask学习

1.环境配置：

    第一步 

        创建项目文件夹：在你的电脑上创建一个新文件夹，比如 my_flask_app。

        在 VS Code 中打开它：在 VS Code 中点击 文件 > 打开文件夹...，选择你刚创建的文件夹。

        小提示：你也可以直接在终端中进入该文件夹，然后输入 code . 命令快速打开。

        打开新终端：在 VS Code 中，点击顶部菜单 终端 > 新建终端，打开一个集成终端窗口。

        创建虚拟环境：在打开的终端中，输入以下命令并按回车，这会创建一个名为 .venv 的虚拟环境文件夹。
    
        Windows上 vscode的终端中输入
        python -m venv .venv

    第二步
        查看 .venv 文件夹下是否有 bin 文件目录，如果有则在终端中输入

        venv\bin\activate

        激活成功后，终端命令行的最前面会出现 (.venv) 的标志，说明你已经处在虚拟环境中了

    第三步
        在终端激活虚拟环境后，输入以下命令来安装 Flask

        在下载flask之前先执行命令

        python -m pip install --upgrade pip

        然后再执行

        pip install flask

        安装完成后，可以输入 
        
        pip list 
        
        查看，确保 flask 已出现在列表中

    第四步
        按下快捷键 Ctrl + Shift + P（macOS 上是 Cmd + Shift + P）打开命令面板。

        输入并选择 Python: Select Interpreter。

        在弹出的列表中，选择带有 ('.venv': venv) 标识的 Python 解释器。

        快速查看：选择成功后，你可以看到 VS Code 窗口左下角会显示 Python 3.x.x ('.venv': venv)，表示当前项目已正确绑定虚拟环境

    第五步
        方式一
            尝试运行app.py
            在vscode的终端中输入
        
            python app.py

            看到输出 Running on     http://127.0.0.1:5000 后， 在浏览器中打开这个地址，就能看到你的“Hello, Flask in VS Code!”

        方式二

            切换到 VS Code 的“运行和调试”视图（点击左侧的“运行和调试”图标，或按 Ctrl+Shift+D）。

            点击“创建 launch.json 文件”，在列表中选择“Flask”。VS Code 会自动生成调试配置。

            然后，直接按 F5 键，应用就会以调试模式运行