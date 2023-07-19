"""Request data check"""

from helpers.codes import INVALID_REQUEST, OK
from helpers.get_non_empty import non_empty_req_fields


def check_request_data(obj, ctx, **kwargs):
    """Validates request data"""

    data = None
    response, code = {}, OK

    try:
        data = obj(**kwargs)
        non_empty_req_fields(data, ctx)

        return response, code, data

    except (KeyError, ValueError) as e:
        response = {
            "code": INVALID_REQUEST,
            "error": getattr(e, 'message', repr(e))
        }
        code = INVALID_REQUEST

        return response, code, data
