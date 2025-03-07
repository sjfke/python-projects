import uuid

import pytest


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


from Person_Decorators import Person

fred = Person(name='Fred', age=35)


def test_get_name_property(p=fred) -> None:
    assert p.name == 'Fred'


def test_get_age_property(p=fred) -> None:
    assert p.age == 35


def test_get_sex_property(p=fred) -> None:
    assert p.sex == 'M'


def test_get_uuid1_property(p=fred) -> None:
    assert is_valid_uuid(p.uuid1)


def test_get_uuid4_property(p=fred) -> None:
    assert is_valid_uuid(p.uuid4)


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


def test_negative_age_property(p=fred) -> None:
    p.age = -1
    assert p.age == 0


def test_excessive_age_property(p=fred) -> None:
    with pytest.raises(ValueError):
        p.age = 151


def test_invalid_gender_property(p=fred) -> None:
    with pytest.raises(ValueError):
        p.sex = 'Non-Binary'


def test_str_representation(p=fred) -> None:
    # 'Person: Fred, 35, M, 64ec8ba8-fab4-11ef-b227-58961dcb95f2, a566d209-aec9-4b31-a629-53a94558082b'
    (_name, _age, _sex, _uuid1, _uuid4) = (p.name, p.age, p.sex, p.uuid1, p.uuid4)
    _result = f"Person: {_name}, {_age}, {_sex}, {_uuid1}, {_uuid4}"
    assert str(p) == _result


def test_repr_representation(p=fred) -> None:
    # "{'name': 'Fred', 'age': '35', 'sex': 'M', 'uuid1': '64ec8ba8-fab4-11ef-b227-58961dcb95f2', 'uuid4': 'a566d209-aec9-4b31-a629-53a94558082b'}"
    _result = f"{{'name': '{p.name}', 'age': '{p.age}', 'sex': '{p.sex}', 'uuid1': '{p.uuid1}', 'uuid4': '{p.uuid4}'}}"
    assert repr(p) == _result
