"""Checks request data"""

from helpers.codes import INVALID_REQUEST, OK
from models.request_method import MethodRequest


def check_request(request, ctx):
    """Verifies request data"""

    code = OK
    response = {}
    ctx["has"] = []

    account = request.get("account", None)
    login = request.get("login", None)
    token = request.get("token", None)
    arguments = request.get("arguments", None)
    method = request.get("method", None)

    try:
        method_req = MethodRequest(
            account=account,
            login=login,
            token=token,
            arguments=arguments,
            method=method
        )

        ctx["is_admin"] = method_req.is_admin

        return response, code

    except (KeyError, ValueError) as e:
        code = INVALID_REQUEST
        response = {
            "code": code,
            "error": getattr(e, 'message', repr(e))
        }

        return response, code
