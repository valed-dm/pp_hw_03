"""Evaluates args of online score request"""

from models.request_fields import GenderField, BirthDayField, PhoneField, EmailField, CharField


class OnlineScoreRequest:
    """Evaluates OnlineScoreRequest"""

    def __init__(self, first_name, last_name, email, phone, birthday, gender):
        self.first_name = CharField(required=False, nullable=True, field=first_name, field_name="first_name")
        self.last_name = CharField(required=False, nullable=True, field=last_name, field_name="last_name")
        self.email = EmailField(required=False, nullable=True, field=email, field_name="email")
        self.phone = PhoneField(required=False, nullable=True, field=phone, field_name="phone")
        self.birthday = BirthDayField(required=False, nullable=True, field=birthday, field_name="birthday")
        self.gender = GenderField(required=False, nullable=True, field=gender, field_name="gender")
