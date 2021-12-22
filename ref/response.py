from fastapi import status
from typing import Optional, Union

status_code_list = {
    200: status.HTTP_200_OK,
    201: status.HTTP_201_CREATED,
    301: status.HTTP_301_MOVED_PERMANENTLY,
    400: status.HTTP_400_BAD_REQUEST,
    401: status.HTTP_401_UNAUTHORIZED,
    404: status.HTTP_404_NOT_FOUND,
    409: status.HTTP_409_CONFLICT,
}

default_msg_list = {
    200: "请求成功",
    201: "已创建",
    301: "请求的资源已被永久的移动到新URI，今后任何新的请求都应使用新的URI代替",
    400: "客户端请求的语法错误，服务器无法理解",
    401: "用户未进行身份认证",
    404: "服务器无法根据客户端的请求找到资源（网页）",
    404: "服务器处理请求时发生了冲突",
}

class CustomException(Exception):
    def __init__(self, code: int, data: Union[list, dict, str], msg: Optional[str] = None):
        self.code = code
        self.data = data
        self.msg = msg