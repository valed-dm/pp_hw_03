"""Evaluates args of clients interests request"""

from models.request_fields import ClientIDsField, DateField


class ClientsInterestsRequest:
    """Evaluates ClientsInterestsRequest"""

    def __init__(self, client_ids, date):
        self.client_ids = ClientIDsField(required=True, nullable=False, field=client_ids, field_name="client_ids")
        self.date = DateField(required=False, nullable=True, field=date, field_name="date")
