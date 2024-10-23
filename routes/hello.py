from flask import Blueprint, jsonify

# 创建一个蓝图
hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route('/hello', methods=['GET'])
def hello_world():  # 这个方法命名不涉及改动其他地方
    """
    示例
    ---
    responses:
      200:
        description: 返回一个问候
        examples:
          application/json: {"message": "Hello, World!"}
    """
    return jsonify(message="Hello, World!")
