from test_travis import __version__
from test_travis.main import add, div


def test_version():
    assert __version__ == '0.1.0'

def test_add():
    assert 3 == add(1, 2)

def test_div():
    assert 2 == div(6, 3)

def test_div_zero():
    assert 1 == div(1, 0)