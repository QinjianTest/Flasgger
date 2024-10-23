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
        "Sign up_au=1.1.977347913.1683357839; "
        "LOCALE=zh-CN; "
        "gxgoldcodeall=64E6206B0B774AC8ACFC1BEE183BDE00; "
        "Sign up_au=1.1.977347913.1683357839; "
        "_gcl_au=1.1.765392397.1683789723; "
        "_gid=GA1.2.193168487.1683517738; "
        "_clck=eixql4|1|fbi|0; "
        "sajssdk_2015_cross_new_user=1; "
        "gxgoldcodeall=F7ABFF7E58C04932B6F99D90E93C414A; "
        "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221CAFEB9CA831BECF31BE4EE840A7C270%22%2C%22first_id%22%3A%2218809b0375d17b4-0affa619fc7d04-26031b51-1327104-18809b0375eb3e%22%2C%22props%22%3A%7B%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4MDliMDM3NWQxN2I0LTBhZmZhNjE5ZmM3ZDA0LTI2MDMxYjUxLTEzMjcxMDQtMTg4MDliMDM3NWViM2UiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxQ0FGRUI5Q0E4MzFCRUNGMzFCRTRFRTg0MEE3QzI3MCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221CAFEB9CA831BECF31BE4EE840A7C270%22%7D%2C%22%24device_id%22%3A%2218809b0375d17b4-0affa619fc7d04-26031b51-1327104-18809b0375eb3e%22%7D; "
        "_fbp=fb.1.1683789757810.1497798901; "
        f"SESSION={session_token}; "  # 动态插入 Session-Token
        "_uetsid=4306e250ed5311edba66e38ea1cb279d; "
        "_uetvid=072e15c0ebba11edbbcf3bead87cba9d; "
        "_ga=GA1.1.846073986.1683341974; "
        "_ga_MEDQG30J5M=GS1.1.1683788601.16.1.1683791257.59.0.0"
    )
    headers = {
        'Accept': 'application/json, text/javascript',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Priority': 'u=1, i',
        'Referer': 'https://www.example.com/boss/site-crm/customer-mt.html',
        'Sec-CH-UA': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'Sec-CH-UA-Mobile': '?0',
        'Sec-CH-UA-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
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
