from thebb_testpackage import myfunction
from thebb_testextension import myfunc


def test_myfunction():
    assert myfunction() == 'test-3'


def test_myfunc():
    assert myfunc() == 'test-3'
