from flask import Flask,redirect
from flasgger import Swagger
from routes import blueprints

app = Flask(__name__)
@app.route('/')
def index():
    # 重定向到 /apidocs
    return redirect('/apidocs')

#配置
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

#页面配置
swagger_template = {
    "info": {
        "title": "TestAPI Hub",  # 修改这里的标题
        "description": "Mitrade测试组的工具平台",
        "version": "1.0.0",  # 修改这里的版本
        "termsOfService": "https://www.example.com/boss/", # 这里设置 Terms of Service 的 URL
        "contact": {
            "email": "xxx@xxx.com",
        },
    }
}
swagger = Swagger(app, config=swagger_config, template=swagger_template) #用来初始化 Flasgger


# 注册蓝图（Blueprint）的主要作用是将应用的不同部分模块化和组织化
# 不使用蓝图 ：所有路由都在一个文件中，适合小型应用。随着应用规模增长，代码可能变得难以维护。
# 使用蓝图 ：路由被分离到不同的模块中，适合大型应用。蓝图提供了模块化的结构，便于维护和扩展。你可以为每个蓝图设置 URL 前缀
for blueprint in blueprints:
    app.register_blueprint(blueprint, url_prefix='/api')

# 启动命令：python app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8732, debug=True)
