import importlib
import pytest
import subprocess
import sys

read_utf8_text = importlib.import_module("read-utf8-text")


@pytest.fixture
def utf8_text() -> str:
    return '''French français médecin deuxième hôtel Noël
German Käse schön über Straße
Portuguese matemática até você saída avó saúde lâmpada não canções França
'''

# https://realpython.com/python-subprocess/#introduction-to-the-shell-and-text-based-programs-with-subprocess
def test_read_utf8_text(capsys, utf8_text):
    filename = './examples/european-words.txt'
    fd = open(filename, 'r', encoding='utf-8')
    result = subprocess.run(
        [sys.executable, "read-utf8-text.py"],
        capture_output=True,
        encoding="utf-8",
        stdin=fd,
        text=True
    )
    fd.close()
    assert result.returncode == 0
    assert result.stdout == utf8_text
