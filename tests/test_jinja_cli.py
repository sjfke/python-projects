import sys
import os
import importlib
import pytest

sys.path.append(os.getcwd() + '/..')
jinja_cli = importlib.import_module("jinja-cli")


@pytest.fixture
def flintstones() -> str:
    return '''FamilyName: Flintstones
  Fred: 30 years old;
  Wilma: 25 years old;
  Pebbles: 1 years old;
  Dino: 5 years old;

FamilyName: Flintstones
      Fred: 30 years old;
     Wilma: 25 years old;
   Pebbles: 01 years old;
      Dino: 05 years old;

'''

@pytest.fixture
def rubbles() -> str:
    return '''FamilyName: rubbles
  barney: 29 years old;
  betty: 26 years old;
  bamm-bamm: 1 years old;
  hoppy: 2 years old;

FamilyName: Rubbles
    Barney: 29 years old;
     Betty: 26 years old;
 Bamm-bamm: 01 years old;
     Hoppy: 02 years old;

'''

def test_assert_true() -> None:
    assert True


def test_output_capture(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

def test_flintstones_json(capsys, flintstones) -> None:
    _template = 'examples/flintstones.txt'
    _parameters = 'examples/flintstones.json' # TODO 'examples/flintstones.yaml'
    _whitespace = False
    _unset_variables = False
    _parameters_format = 'json_format'

    jinja_cli.render_template(template_filename=_template, parameters_filename=_parameters,
                                     whitespace=_whitespace,
                                     unset_variables=_unset_variables,
                                     file_format=_parameters_format)
    captured = capsys.readouterr()
    assert captured.out == flintstones


def test_flintstones_yaml(capsys, flintstones) -> None:
    _template = 'examples/flintstones.txt'
    _parameters = 'examples/flintstones.yaml'
    _whitespace = False
    _unset_variables = False
    _parameters_format = 'yaml_format'

    jinja_cli.render_template(template_filename=_template, parameters_filename=_parameters,
                                     whitespace=_whitespace,
                                     unset_variables=_unset_variables,
                                     file_format=_parameters_format)
    captured = capsys.readouterr()
    assert captured.out == flintstones


def test_rubbles_json(capsys, rubbles) -> None:
    _template = 'examples/rubbles.txt'
    _parameters = 'examples/rubbles.json'
    _whitespace = False
    _unset_variables = False
    _parameters_format = 'json_format'

    jinja_cli.render_template(template_filename=_template, parameters_filename=_parameters,
                                     whitespace=_whitespace,
                                     unset_variables=_unset_variables,
                                     file_format=_parameters_format)
    captured = capsys.readouterr()
    assert captured.out == rubbles

def test_rubbles_yaml(capsys, rubbles) -> None:
    _template = 'examples/rubbles.txt'
    _parameters = 'examples/rubbles.yaml'
    _whitespace = False
    _unset_variables = False
    _parameters_format = 'yaml_format'

    jinja_cli.render_template(template_filename=_template, parameters_filename=_parameters,
                                     whitespace=_whitespace,
                                     unset_variables=_unset_variables,
                                     file_format=_parameters_format)
    captured = capsys.readouterr()
    assert captured.out == rubbles
