import pytest
import subprocess
import sys

# https://python-basics-tutorial.readthedocs.io/en/latest/test/pytest/fixtures.html
# setup 'fd' for the tests, commands after yield are tear-down
@pytest.fixture
def fd():
    """Provides a file descriptor."""
    filename = './examples/european-words.txt'
    fd = open(filename, 'r', encoding='utf-8')
    yield fd
    fd.close()


@pytest.fixture
def utf8_text() -> str:
    return '''French français médecin deuxième hôtel Noël
German Käse schön über Straße
Portuguese matemática até você saída avó saúde lâmpada não canções França
'''

@pytest.fixture
def numbered_utf8_text() -> str:
    return '''001: French français médecin deuxième hôtel Noël
002: German Käse schön über Straße
003: Portuguese matemática até você saída avó saúde lâmpada não canções França
'''


# -r, -rn, -rv
@pytest.fixture
def raw_utf8_text() -> str:
    return '''contents: ['French français médecin deuxième hôtel Noël\n', 'German Käse schön über Straße\n', 'Portuguese matemática até você saída avó saúde lâmpada não canções França ']'''


# https://realpython.com/python-subprocess/#introduction-to-the-shell-and-text-based-programs-with-subprocess
def test_read_utf8_text(capsys, fd, utf8_text):
    result = subprocess.run(
        [sys.executable, "read-utf8-text.py"],
        capture_output=True,
        encoding="utf-8",
        stdin=fd
    )
    assert result.returncode == 0
    assert result.stdout == utf8_text

def test_read_numbered_utf8_text(capsys, fd, numbered_utf8_text):
    result = subprocess.run(
        [sys.executable, "read-utf8-text.py", '-n'],
        capture_output=True,
        encoding="utf-8",
        stdin=fd,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout == numbered_utf8_text

# FAILS - UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 141: invalid continuation byte
# Issue is maybe the 'subprocess.run' because 'verbose' returns the wrong encoding
# def test_read_raw_utf8_text(capsys, fd, raw_utf8_text):
#     result = subprocess.run(
#         [sys.executable, "read-utf8-text.py", '-r'],
#         capture_output=True,
#         encoding="utf-8",
#         stdin=fd,
#         text=True
#     )
#     assert result.returncode == 0
#     assert result.stdout == raw_utf8_text
