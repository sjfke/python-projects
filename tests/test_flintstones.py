import importlib
import pytest

flintstones = importlib.import_module("flintstones")

@pytest.fixture
def error_message() -> str:
    return '''KeyError: fred not found
'''

def test_flintstones_get_names() -> None:
    assert ['Fred', 'Wilma', 'Pebbles', 'Dino'] == flintstones.get_names()


def test_flintstones_get_ages() -> None:
    assert [30, 25, 1, 5] == flintstones.get_ages()


def test_flintstones_good_person() -> None:
    assert {'Fred': 30} == flintstones.get_person(name='Fred')


def test_flintstones_bad_person(capsys, error_message) -> None:
    flintstones.get_person(name='fred')
    captured = capsys.readouterr()
    assert captured.err == error_message
