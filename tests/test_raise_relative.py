import force_absolute_imports
import pytest


@pytest.mark.parametrize('line', (
    'from . import x',
    'from. import x',
    'from.import x',
    'from .import x',
    'from .. import x',
    'from .foo import x',
    'from .foo.bar import x',
    'from.foo.bar import x',
    'from ..foo.bar import x',
))
def test_raise_relative(line):
    assert not force_absolute_imports.only_absolute_line(line)


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
    assert force_absolute_imports.only_absolute_line(line)
