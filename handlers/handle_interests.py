"""Clients interests request handler"""

from check.check_request_data import check_request_data
from helpers.codes import INVALID_REQUEST
from helpers.get_set_interests import get_interests
from models.request_interests import ClientsInterestsRequest


def clients_interests_handler(request, ctx):
    """Handles clients interests request"""

    arguments = request["body"]["arguments"]
    client_ids = arguments.get("client_ids", None)
    date = arguments.get("date", None)

    response, code, _ = check_request_data(
        obj=ClientsInterestsRequest, ctx=ctx, client_ids=client_ids, date=date
    )

    if code != INVALID_REQUEST:
        ctx["nclients"] = len(client_ids)

        for cid in client_ids:
            interests = get_interests(cid=cid)
            response[f"{cid}"] = interests

    return response, code
