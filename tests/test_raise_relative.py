import force_absolute_imports
import pytest


@pytest.mark.parametrize('line', (
    'from . import x',
    'from .. import x',
    'from .foo import x',
    'from .foo.bar import x',
    'from ..foo.bar import x',
))
def test_raise_relative(line):
    with pytest.raises(ValueError) as pytest_wrapped_e:
        force_absolute_imports.check_line(line)

@pytest.mark.parametrize('line', (
    'from lib import x',
    'from lib import x as renamed',
    'from lib.foo import x',
    'import lib',
    'import lib as renamed',
    'import lib.foo'
    'import lib.foo as renamed'
))
def test_pass_absolute(line):
    force_absolute_imports.check_line(line)


@pytest.mark.xfail(reason='todo')
def test_print_location(capsys):
    raise


def test_only_py_files():
    with pytest.raises(ValueError):
        force_absolute_imports.check_file('file.java')
