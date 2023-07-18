"""Evaluates if object keys has non-empty values """


def non_empty_req_fields(obj, ctx):
    """Context dict gets list of non-empty API request values"""

    for _, value in vars(obj).items():  # _ is used for attribute substitution to avoid pylint warning "unused argument"
        if value.field is not None:
            ctx["has"].append(value.field_name)
