"""Authentication check"""

import datetime
import hashlib

from helpers.codes import ADMIN_LOGIN, ADMIN_SALT, SALT


def check_auth(request):
    """Checks if user is authenticated"""

    if request.get("login", "") == ADMIN_LOGIN:
        digest = hashlib.sha512(
            (datetime.datetime.now().strftime("%Y%m%d%H") + ADMIN_SALT)
            .encode("utf-8")
        ).hexdigest()
        # for use when testing
        # request["token"] = digest
        # print(digest)
    else:
        digest = hashlib.sha512(
            (request.get("account", "") + request.get("login", "") + SALT)
            .encode("utf-8")
        ).hexdigest()
        # for use when testing
        # request["token"] = digest
        # print(digest)
    if digest == request.get("token", None):
        return True
    return False
