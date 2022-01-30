import pytest

import force_absolute_imports


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
    '    from . import x',
    '    from ..foo import x',
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
    '    from lib import x',
))
def test_pass_absolute(line):
    assert force_absolute_imports.only_absolute_line(line)


@pytest.mark.xfail
def test_bad_file(capsys):
    assert not force_absolute_imports.only_absolute_file('unfixed_src/bad.py')
    out, err = capsys.readouterr()
    assert out == 'relative import: unfixed_src/bad.py:1 from .x import foo\n'


def test_good_file(capsys):
    assert force_absolute_imports.only_absolute_file('unfixed_src/good.py')
    out, err = capsys.readouterr()
    assert out == ''
