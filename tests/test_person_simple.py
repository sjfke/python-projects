import pytest

import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


# ------------------------------------------------------------------ #
# NOTE: '.__uuid4' is not accessible using 'pytest', so not testable #
# ------------------------------------------------------------------ #

from Person_Simple import Person

fred = Person(name='Fred', age=35)


def test_get_name_property(p=fred) -> None:
    assert p.name == 'Fred'


def test_get_age_property(p=fred) -> None:
    assert p.age == 35


def test_get_sex_property(p=fred) -> None:
    assert p.sex == 'M'


def test_get_uuid1_property(p=fred) -> None:
    assert is_valid_uuid(p._uuid1)


def test_set_name_property(p=fred) -> None:
    p.name = 'Freddie'
    assert p.name == 'Freddie'


def test_set_age_property(p=fred) -> None:
    p.age = 36
    assert p.age == 36


def test_negative_age_exception() -> None:
    with pytest.raises(ValueError):
        _p = Person(name='Fred', age=-1)


def test_excessive_age_exception() -> None:
    with pytest.raises(ValueError):
        _p = Person(name='Fred', age=151)


def test_invalid_gender_exception() -> None:
    with pytest.raises(ValueError):
        _p = Person(name='Fred', age=35, sex='Non-Binary')


def test_str_representation(p=fred) -> None:
    # 'Person: Fred, 35, M, e9f29638-e992-4d1f-a236-db4961782829'
    (_name, _age, _sex, _uuid1) = (p.name, p.age, p.sex, p._uuid1)
    assert str(p) == f"Person: {_name}, {_age}, {_sex}, {_uuid1}"


def test_repr_representation(p=fred) -> None:
    # "{'name': Fred, 'age': '35', 'sex': M, '_uuid1': e9f29638-e992-4d1f-a236-db4961782829}"
    assert repr(p) == f"{{'name': '{p.name}', 'age': '{p.age}', 'sex': '{p.sex}', '_uuid1': '{p._uuid1}'}}"
