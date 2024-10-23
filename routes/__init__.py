# 这个文件可以留空，主要作用是将一个目录标识为一个 Python 包，
# 保持与 Python 2 的兼容性
# 便于复杂项目，明确哪些模块应该被导入
from .hello import hello_blueprint
from .user_search import users_blueprint

# 可以在这里创建一个蓝图列表，便于统一注册
blueprints = [hello_blueprint,users_blueprint]
