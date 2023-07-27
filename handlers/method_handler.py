"""Request validation and handler"""

import logging

from check.check_auth import check_auth
from check.check_request import check_request
from helpers.codes import INTERNAL_ERROR, INVALID_REQUEST, FORBIDDEN, OK
from routes.api_routes import router


def method_handler(request, headers, context):
    """Validates and routes request to a handler"""

    response, code = {}, OK

    if request:
        # request check authentication
        is_auth = check_auth(request)

        if is_auth:
            # request validation
            response, code = check_request(request=request, ctx=context)

            # handle request
            if request.get("method", None) in router and not response:
                try:
                    response, code = router[request["method"]](
                        {"body": request, "headers": headers}, context
                    )
                except Exception as e:
                    logging.exception("Unexpected error: %s", e)
                    code = INTERNAL_ERROR
            else:
                code = INVALID_REQUEST

        # when authentication failed
        if not is_auth:
            code = FORBIDDEN
            response = {"code": code, "error": "Forbidden"}

    else:
        code = INVALID_REQUEST

    return response, code
