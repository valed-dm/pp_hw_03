"""Classes for request's fields data evaluation"""


import datetime

from helpers.codes import ADMIN_LOGIN


class Field:
    """Evaluates all fields for required, nullable"""

    def __init__(self, field, field_name, required, nullable):

        if required and field is None:
            raise KeyError(f"request {repr(field_name)} field is required but not found")

        if not field:
            if nullable:
                pass
            else:
                raise ValueError(f"{field_name} must contain value")

        self.field = field
        self.field_name = field_name


class CharField(Field):
    """Evaluates CharField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)

        if not isinstance(field, str) and field is not None:
            raise ValueError(f"{field_name} must be of 'str' type, not {field}")


class ArgumentsField(Field):
    """Evaluates ArgumentsField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)

        if field:
            if not isinstance(field, dict):
                raise ValueError("arguments must be of dict type")


class EmailField(Field):
    """Evaluates EmailField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)

        if field:
            if not isinstance(field, str) or '@' not in field and field:
                raise ValueError(f"{field_name} string must contain '@', {field} is not valid")


class PhoneField(Field):
    """Evaluates PhoneField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)

        if field:
            phone = str(field)
            if len(phone) not in [0, 11]:
                raise ValueError(
                    f"phone should contain 11 digits with leading '7' or left empty, not {phone}"
                )
            if not phone.startswith("7") and len(phone) != 0:
                raise ValueError(
                    f"phone should contain 11 digits with leading '7' or left empty, not {phone}"
                )


class DateField(Field):
    """Evaluates DateField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)
        date_format = "%d.%m.%Y"
        if field:
            try:
                datetime.datetime.strptime(field, date_format)
            except ValueError as e:
                raise ValueError(f"date format 'DD.MM.YYYY' or empty: {field} is not valid") from e


class BirthDayField(Field):
    """Evaluates BirthdayField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)
        date_format = "%d.%m.%Y"
        if field:
            try:
                b_date_time = datetime.datetime.strptime(field, date_format)
            except ValueError as e:
                raise ValueError(f"date format 'DD.MM.YYYY' or empty: {field} is not valid") from e

            now_time = datetime.datetime.now()
            t_delta_years = now_time.year - b_date_time.year
            if t_delta_years >= 70:
                raise ValueError(f"person age should not exceed 70, but given {t_delta_years}")


class GenderField(Field):
    """Evaluates GenderField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)
        if field is not None:
            if not isinstance(field, int) and field not in [0, 1, 2] or field < 0:
                raise ValueError(f"gender value should be integer of 0, 1, 2 or left empty, not {repr(field)}")


class ClientIDsField(Field):
    """Evaluates ClientsIDsField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)
        if not isinstance(field, list) or len(field) == 0:
            raise ValueError(f"client_ids should be of non-empty list type, not {repr(field)}")
        if not all(isinstance(item, int) for item in field):
            raise ValueError(f"all client_ids values are to be integers, not {repr(field)}")


class ClientsInterestsRequest:
    """Evaluates ClientsInterestsRequest"""

    def __init__(self, client_ids, date):
        self.client_ids = ClientIDsField(required=True, nullable=False, field=client_ids, field_name="client_ids")
        self.date = DateField(required=False, nullable=True, field=date, field_name="date")


class OnlineScoreRequest:
    """Evaluates OnlineScoreRequest"""

    def __init__(self, first_name, last_name, email, phone, birthday, gender):
        self.first_name = CharField(required=False, nullable=True, field=first_name, field_name="first_name")
        self.last_name = CharField(required=False, nullable=True, field=last_name, field_name="last_name")
        self.email = EmailField(required=False, nullable=True, field=email, field_name="email")
        self.phone = PhoneField(required=False, nullable=True, field=phone, field_name="phone")
        self.birthday = BirthDayField(required=False, nullable=True, field=birthday, field_name="birthday")
        self.gender = GenderField(required=False, nullable=True, field=gender, field_name="gender")


class MethodRequest:
    """Evaluates MethodRequest"""

    def __init__(self, account, login, token, method, arguments):
        self.account = CharField(required=False, nullable=True, field=account, field_name="account")
        self.login = CharField(required=True, nullable=True, field=login, field_name="login")
        self.token = CharField(required=True, nullable=True, field=token, field_name="token")
        self.method = CharField(required=True, nullable=True, field=method, field_name="method")
        self.arguments = ArgumentsField(required=True, nullable=False, field=arguments, field_name="arguments")

    @property
    def is_admin(self):
        """Checks if request login is 'admin'"""
        return self.login.field == ADMIN_LOGIN
