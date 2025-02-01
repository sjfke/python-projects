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
    p.set_name('Freddy')
    assert p.get_name() == 'Freddy'


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
