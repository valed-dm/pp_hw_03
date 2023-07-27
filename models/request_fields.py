"""Classes for request fields data evaluation"""

import datetime


class Field:
    """Evaluates all fields for required, nullable"""

    def __init__(self, field, field_name, required, nullable):
        self.field = self._is_valid(field, field_name, required, nullable)
        self.field_name = field_name

    @staticmethod
    def _is_valid(field, field_name, required, nullable):
        if required and field is None:
            raise KeyError(f"request {repr(field_name)} field is required")
        if not field:
            if nullable:
                pass
            else:
                raise ValueError(f"{field_name} must contain value")
        return field


class CharField(Field):
    """Evaluates CharField"""

    def __init__(self, field, field_name, required, nullable):
        super().__init__(field, field_name, required, nullable)
        self._is_valid_charfield(field, field_name)

    @staticmethod
    def _is_valid_charfield(field, field_name):
        if not isinstance(field, str) and field is not None:
            raise ValueError(f"{field_name} must be of 'str' type, not {field}")


class ArgumentsField(Field):
    """Evaluates ArgumentsField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        if field is not None:
            if not isinstance(field, dict):
                raise ValueError(f"ArgumentsField must be of 'dict' type, not {field}")
        self._field = field


class EmailField(Field):
    """Evaluates EmailField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        if field is not None:
            if not isinstance(field, str) or "@" not in field:
                raise ValueError(f"email must contain '@', {field} is not valid")
        self._field = field


class PhoneField(Field):
    """Evaluates PhoneField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        if field is not None:
            if isinstance(field, (str, int)):
                phone = str(field)
                if len(phone) not in [0, 11]:
                    raise ValueError(
                        f"phone should contain 11 digits with leading '7' or left empty, not {phone}"
                    )
                if not phone.startswith("7") and len(phone) != 0:
                    raise ValueError(
                        f"phone should contain 11 digits with leading '7' or left empty, not {phone}"
                    )
            else:
                raise ValueError(f"phone should be of str or int type, not {field}")

        self._field = field


class DateField(Field):
    """Evaluates DateField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        date_format = "%d.%m.%Y"
        if field is not None:
            if field != "":
                try:
                    datetime.datetime.strptime(field, date_format)
                except (ValueError, TypeError) as e:
                    raise ValueError(
                        f"date format 'DD.MM.YYYY' or empty: {repr(field)} is not valid"
                    ) from e
        self._field = field


class BirthDayField(Field):
    """Evaluates BirthdayField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        date_format = "%d.%m.%Y"
        if field is not None:
            if field != "":
                try:
                    b_date_time = datetime.datetime.strptime(field, date_format)
                except (ValueError, TypeError) as e:
                    raise ValueError(
                        f"birthday format 'DD.MM.YYYY' or empty: {field} is not valid"
                    ) from e

                now_time = datetime.datetime.now()
                t_delta_years = now_time.year - b_date_time.year
                if t_delta_years >= 70:
                    raise ValueError(
                        f"person age should not exceed 70, but given {t_delta_years}"
                    )
        self._field = field


class GenderField(Field):
    """Evaluates GenderField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        if field is not None:
            if not isinstance(field, int) or field not in [0, 1, 2] or field < 0:
                raise ValueError(
                    f"gender is pos integer of 0, 1, 2 or left empty, not {repr(field)}"
                )
        self._field = field


class ClientIDsField(Field):
    """Evaluates ClientsIDsField"""

    @property
    def field(self):
        """Property object setter is used for field validation"""
        return self._field

    @field.setter
    def field(self, field):
        if not isinstance(field, list) or len(field) == 0:
            raise ValueError(
                f"client_ids should be of non-empty list type, not {repr(field)}"
            )
        if not all(isinstance(item, int) for item in field):
            raise ValueError(
                f"all client_ids values are to be integers, not {repr(field)}"
            )
        self._field = field
