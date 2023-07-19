"""API request evaluation"""

from helpers.codes import ADMIN_LOGIN
from models.request_fields import CharField, ArgumentsField


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
