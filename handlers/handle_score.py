"""Score request handler"""

from helpers.codes import INVALID_REQUEST, OK
from helpers.get_non_empty import non_empty_req_fields
from helpers.get_score import get_score
from models.request_score import OnlineScoreRequest


def online_score_handler(request, ctx):
    """Handles score request"""

    code = OK

    req = request.get("body", None)
    arguments = req.get("arguments", None)
    first, last, email, phone, birthday, gender = ("" for _ in range(6))

    if not ctx["is_admin"]:
        # to pass when arguments=None:
        if arguments:
            first = arguments.get("first_name", None)
            last = arguments.get("last_name", None)
            email = arguments.get("email", None)
            phone = arguments.get("phone", None)
            birthday = arguments.get("birthday", None)
            gender = arguments.get("gender", None)

        if (first and last) or (email and phone) or (birthday and gender is not None):
            try:
                data = OnlineScoreRequest(
                    first_name=first,
                    last_name=last,
                    email=email,
                    phone=phone,
                    birthday=birthday,
                    gender=gender
                )
                non_empty_req_fields(data, ctx)

            except (KeyError, ValueError) as e:
                response = {
                    "code": INVALID_REQUEST,
                    "error": getattr(e, 'message', repr(e))
                }
                code = INVALID_REQUEST
                return response, code

            score = get_score(
                store=None,
                phone=data.phone.field,
                email=data.email.field,
                birthday=data.birthday.field,
                gender=data.gender.field,
                first_name=data.first_name.field,
                last_name=data.last_name.field
            )
            response = {"score": score}

        else:
            code = INVALID_REQUEST
            response = {
                "code": code,
                "error": "args must contain albeit one non-empty values pair: "
                         "phone/email, "
                         "first/last name, "
                         "gender/birthday, "
                         f"but got {arguments}"
            }
    else:
        response = {"score": 42}

    return response, code
