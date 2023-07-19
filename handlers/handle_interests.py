"""Clients interests request handler"""

from helpers.codes import INVALID_REQUEST, OK
from helpers.get_interests import get_interests
from helpers.get_non_empty import non_empty_req_fields
from models.request_interests import ClientsInterestsRequest


def clients_interests_handler(request, ctx):
    """Handles clients interests request"""

    code = OK
    response = {}

    arguments = request["body"]["arguments"]
    client_ids = arguments.get("client_ids", None)
    date = arguments.get("date", None)

    # request data validates here:
    try:
        data = ClientsInterestsRequest(client_ids=client_ids, date=date)
        non_empty_req_fields(data, ctx)

    except (KeyError, ValueError) as e:
        response = {
            "code": INVALID_REQUEST,
            "error": getattr(e, 'message', repr(e))
        }
        code = INVALID_REQUEST
        return response, code

    ctx["nclients"] = len(client_ids)

    for cid in client_ids:
        interests = get_interests(store=None, cid=cid)
        response[f"{cid}"] = interests

    return response, code
