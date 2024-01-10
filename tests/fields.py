"""Fields tests data"""

field_data = [
    (None, True, True, "\"request 'Field' field is required\""),
    (None, True, False, "\"request 'Field' field is required\""),
    (None, False, False, "Field must contain value"),
    (None, False, True, None),
    ({}, True, True, {}),
    ({}, True, False, "Field must contain value"),
    ({}, False, False, "Field must contain value"),
    ({}, False, True, {}),
    ([], True, False, "Field must contain value"),
    ((), True, False, "Field must contain value"),
    ("", True, False, "Field must contain value"),
    ("test_0", True, True, "test_0"),
    ("test_1", True, False, "test_1"),
    ("test_2", False, False, "test_2"),
    ("test_3", False, True, "test_3"),
]

charfield_data = [
    (None, "\"request 'CharField' field is required\""),
    ({}, "CharField must be of 'str' type, not {}"),
    ([], "CharField must be of 'str' type, not []"),
    ((), "CharField must be of 'str' type, not ()"),
    ("test", "test"),
    ("", ""),
]

arguments_data = [
    (None, "\"request 'ArgumentsField' field is required\""),
    ([], "ArgumentsField must be of 'dict' type, not []"),
    ((), "ArgumentsField must be of 'dict' type, not ()"),
    ("", "ArgumentsField must be of 'dict' type, not "),
    ({"test": "test"}, {"test": "test"}),
    ({}, {}),
]

email_data = [
    (None, "\"request 'EmailField' field is required\""),
    ({}, "email must contain '@', {} is not valid"),
    ([], "email must contain '@', [] is not valid"),
    ((), "email must contain '@', () is not valid"),
    ("", "email must contain '@',  is not valid"),
    ("test", "email must contain '@', test is not valid"),
    ("", "email must contain '@',  is not valid"),
    ("@", "@"),
]

phone_data = [
    (None, "\"request 'PhoneField' field is required\""),
    ({}, "phone should be of str or int type, not {}"),
    ([], "phone should be of str or int type, not []"),
    ((), "phone should be of str or int type, not ()"),
    ("1", "phone should contain 11 digits with leading '7' or left empty, not 1"),
    (
        "+79789445115",
        "phone should contain 11 digits with leading '7' or left empty, not +79789445115",
    ),
    ("79789445115", "79789445115"),
    (79789445115, 79789445115),
    ("", ""),
]

date_data = [
    (None, "\"request 'DateField' field is required\""),
    ({}, "date format 'DD.MM.YYYY' or empty: {} is not valid"),
    ([], "date format 'DD.MM.YYYY' or empty: [] is not valid"),
    ((), "date format 'DD.MM.YYYY' or empty: () is not valid"),
    ("20-12-2022", "date format 'DD.MM.YYYY' or empty: '20-12-2022' is not valid"),
    ("20.12.2022", "20.12.2022"),
    ("", ""),
]

birthday_data = [
    (None, "\"request 'BirthDayField' field is required\""),
    ({}, "birthday format 'DD.MM.YYYY' or empty: {} is not valid"),
    ([], "birthday format 'DD.MM.YYYY' or empty: [] is not valid"),
    ((), "birthday format 'DD.MM.YYYY' or empty: () is not valid"),
    ("20-12-2022", "birthday format 'DD.MM.YYYY' or empty: 20-12-2022 is not valid"),
    ("20.12.1979", "20.12.1979"),
    ("20.12.1939", "person age should not exceed 70, but given 85"),
    ("", ""),
]

gender_data = [
    (None, "\"request 'GenderField' field is required\""),
    ({}, "gender is pos integer of 0, 1, 2 or left empty, not {}"),
    ([], "gender is pos integer of 0, 1, 2 or left empty, not []"),
    ((), "gender is pos integer of 0, 1, 2 or left empty, not ()"),
    ("", "gender is pos integer of 0, 1, 2 or left empty, not ''"),
    (0, 0),
    (1, 1),
    (2, 2),
    (3, "gender is pos integer of 0, 1, 2 or left empty, not 3"),
    (-2, "gender is pos integer of 0, 1, 2 or left empty, not -2"),
]

client_ids_data = [
    (None, "\"request 'ClientIDsField' field is required\""),
    ({}, "client_ids should be of non-empty list type, not {}"),
    ([], "client_ids should be of non-empty list type, not []"),
    ((), "client_ids should be of non-empty list type, not ()"),
    ("", "client_ids should be of non-empty list type, not ''"),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2, "key"], "all client_ids values are to be integers, not [1, 2, 'key']"),
    ([1, 2, {"key": "value"}], "all client_ids values are to be integers, not [1, 2, {'key': 'value'}]"),
]
