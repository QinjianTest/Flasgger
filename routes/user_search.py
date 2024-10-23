from flask import Blueprint, jsonify,request
from common.login import login_to_service,search

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['POST'])
def login():
    # 调用登录函数
    # parameters -name为输入参数
    """
    输入email，查询用户信息
    ---
    parameters:
      - name: email
        in: query
        type: string
        required: true
        description: 点击Try it out，输入要查询的email
    responses:
      200:
        description: 调用Boss接口，查询用户信息
        examples:
          application/json:
              用户信息:
                    GUID: "test12CE88404E12BB44D324FC5A6809"
                    交易组别: "USD_XXX_XXXX"
                    国家: "XX"
                    牌照: "XXXX"
                    用户名: "testuser"
                    邮箱: "testuser@xxxhi.cc"
    """
    email = request.args.get('email')
    if not email:
        return jsonify({"error": "Email is required"}), 400

    login_response = login_to_service('user', 'PWD', '')
    search_response = search(login_response,email)

    #提取返回的数据
    client_info = search_response["value"]["resultList"][0]
    response = {
        "用户信息": {
            "用户名": client_info.get("clientName"),
            "邮箱": client_info.get("email"),
            "牌照": client_info.get("financialLicense"),
            "GUID": client_info.get("customerId"),
            "国家": client_info.get("nationality"),
            "交易组别": client_info.get("groupName"),
            }
        }
    return jsonify(response)