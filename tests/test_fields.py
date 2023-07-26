"""Tests all request fields constraints"""

import pytest

from fields import *
from models.request_fields import (
    Field,
    CharField,
    ArgumentsField,
    EmailField,
    PhoneField,
    DateField,
    BirthDayField,
    GenderField,
    ClientIDsField,
)


@pytest.mark.parametrize("field, required, nullable, expected", field_data)
class TestField:
    """Test covers all request's fields 'required', 'nullable' attrs"""

    def test_field(self, field, required, nullable, expected):
        """Field"""

        field_name = "Field"

        try:
            f = Field(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "Field"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", charfield_data)
class TestCharField:
    """Test for CharField"""

    def test_charfield(self, field, expected):
        """CharField"""

        field_name = "CharField"
        required = True
        nullable = True

        try:
            f = CharField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "CharField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", arguments_data)
class TestArgumentsField:
    """Test for ArgumentsField"""

    def test_arguments(self, field, expected):
        """ArgumentsField"""

        field_name = "ArgumentsField"
        required = True
        nullable = True

        try:
            f = ArgumentsField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "ArgumentsField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", email_data)
class TestEmailField:
    """Test for EmailField"""

    def test_email(self, field, expected):
        """EmailField"""

        field_name = "EmailField"
        required = True
        nullable = True

        try:
            f = EmailField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "EmailField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", phone_data)
class TestPhoneField:
    """Test for PhoneField"""

    def test_phone(self, field, expected):
        """PhoneField"""

        field_name = "PhoneField"
        required = True
        nullable = True

        try:
            f = PhoneField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "PhoneField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", date_data)
class TestDateField:
    """Test for DateField"""

    def test_date(self, field, expected):
        """DateField"""

        field_name = "DateField"
        required = True
        nullable = True

        try:
            f = DateField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "DateField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", birthday_data)
class TestBirthDayField:
    """Test for BirthDayField"""

    def test_birthday(self, field, expected):
        """BirthDayField"""

        field_name = "BirthDayField"
        required = True
        nullable = True

        try:
            f = BirthDayField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "BirthDayField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", gender_data)
class TestGenderField:
    """Test for GenderField"""

    def test_gender(self, field, expected):
        """GenderField"""

        field_name = "GenderField"
        required = True
        nullable = True

        try:
            f = GenderField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "GenderField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected


@pytest.mark.parametrize("field, expected", client_ids_data)
class TestClientIDsField:
    """Test for ClientIDsField"""

    def test_gender(self, field, expected):
        """ClientIDsField"""

        field_name = "ClientIDsField"
        required = True
        nullable = True

        try:
            f = ClientIDsField(field, field_name, required, nullable)
            assert f.field == expected
            assert f.field_name == "ClientIDsField"
        except (KeyError, ValueError) as e:
            assert getattr(e, "message", str(e)) == expected
