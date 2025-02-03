import importlib
import pytest

import uuid


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


from Person import Person

fred = Person(name='Fred', age=35)


def test_get_name_property(p=fred) -> None:
    assert p.name == 'Fred'


def test_get_name_getter(p=fred) -> None:
    assert p.get_name() == 'Fred'


def test_get_age_property(p=fred) -> None:
    assert p.age == 35


def test_get_age_getter(p=fred) -> None:
    assert p.get_age() == 35


def test_get_sex_property(p=fred) -> None:
    assert p.sex == 'M'


def test_get_sex_getter(p=fred) -> None:
    assert p.get_sex() == 'M'


def test_get_uuid_property(p=fred) -> None:
    assert is_valid_uuid(p.uuid)


def test_get_uuid_getter(p=fred) -> None:
    assert is_valid_uuid(p.get_uuid())


def test_set_name_property(p=fred) -> None:
    p.name = 'Freddie'
    assert p.name == 'Freddie'


def test_set_name_setter(p=fred) -> None:
    p.set_name('Fred')
    assert p.get_name() == 'Fred'


def test_set_age_property(p=fred) -> None:
    p.age = 36
    assert p.age == 36


def test_set_age_setter(p=fred) -> None:
    p.set_age(37)
    assert p.get_age() == 37


def test_set_age_zero_property(p=fred) -> None:
    p.age = -1
    assert p.age == 0


def test_set_age_zero_setter(p=fred) -> None:
    p.set_age(-1)
    assert p.get_age() == 0


def test_set_age_property_exception(p=fred) -> None:
    with pytest.raises(ValueError):
        p.age = '35'


def test_set_age_setter_exception(p=fred) -> None:
    with pytest.raises(ValueError):
        p.set_age('35')


def test_str_representation(p=fred) -> None:
    # 'Person: Fred, 35, M, e9f29638-e992-4d1f-a236-db4961782829'
    (_name, _age, _sex, _uuid) = (p.name, p.age, p.sex, p.uuid)
    assert str(p) == f"Person: {_name}, {_age}, {_sex}, {_uuid}"


def test_repr_representation(p=fred) -> None:
    # "{'name': Fred, 'age': 35, 'sex': M, 'uuid': e9f29638-e992-4d1f-a236-db4961782829}"
    assert repr(p) == f"{{'name': '{p.name}', 'age': {p.age}, 'sex': '{p.sex}', 'uuid': '{p.uuid}'}}"
