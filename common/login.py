import requests
import logging

# 配置日志记录
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 创建一个日志记录器
logger = logging.getLogger(__name__)


def login_to_service(account, password, google_code=''):
    url = "https://www.example.com/boss/login"
    payload = {
        'account': account,
        'password': password,
        'googleCode': google_code
    }
    try:
        logger.debug("Sending login request to %s with payload: %s", url, payload)
        response = requests.post(url, data=payload)
        logger.debug("Received response: %s", response.text)
        response.raise_for_status()
        session_token = response.headers.get('Session-Token')
        if session_token:
            logger.debug("Session-Token received: %s", session_token)
            return session_token
        else:
            logger.warning("Session-Token not found in response headers")
            return None
    except requests.exceptions.RequestException as e:
        logger.error("Error during login request: %s", e)
        return None



def search(session_token,email):
    url = "https://www.example.com/boss/crm/base/full"
    params = {
        'email': email,
        'pageSize': 20,
        'currentPage': 1
    }
    cookies = (
        f"SESSION={session_token}; "  # 动态插入 Session-Token
    )
    headers = {
        'Accept': 'application/json, text/javascript',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookies

    }
    try:
        logger.debug("Sending data fetch request to %s with headers: %s and params: %s", url, headers, params)
        response = requests.get(url, headers=headers, params=params)
        logger.debug("Received response: %s", response.text)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error("Error during data fetch request: %s", e)
        return {"error": str(e)}
