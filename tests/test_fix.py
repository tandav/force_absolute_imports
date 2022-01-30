from pathlib import Path

import pytest

import force_absolute_imports


@pytest.mark.parametrize('line, result', (
    ('from . import x\n', {'s0': '', 's1': ' ', 'dots': '.', 's2': ' ', 'rest': 'import x\n'}),
    ('from .. import x\n', {'s0': '', 's1': ' ', 'dots': '..', 's2': ' ', 'rest': 'import x\n'}),
    ('from .foo import x\n', {'s0': '', 's1': ' ', 'dots': '.', 's2': '', 'rest': 'foo import x\n'}),
    ('from.foo import x\n', {'s0': '', 's1': '', 'dots': '.', 's2': '', 'rest': 'foo import x\n'}),
    ('from .foo.bar import x\n', {'s0': '', 's1': ' ', 'dots': '.', 's2': '', 'rest': 'foo.bar import x\n'}),
    ('from ..foo.bar import x\n', {'s0': '', 's1': ' ', 'dots': '..', 's2': '', 'rest': 'foo.bar import x\n'} ),
    ('    from .. import x\n', {'s0': '    ', 's1': ' ', 'dots': '..', 's2': ' ', 'rest': 'import x\n'}),
))
def test_parse(line, result):
    assert force_absolute_imports.parse(line) == result


@pytest.mark.parametrize('file, line, fixed', (
    ('unfixed_src/bad_module/some.py', 'from . import x\n', 'from unfixed_src.bad_module import x\n'),
    ('unfixed_src/bad_module/some.py', 'from .. import x\n', 'from unfixed_src import x\n'),
    ('unfixed_src/bad_module/some.py', 'from ..foo import x\n', 'from unfixed_src.foo import x\n'),
    ('unfixed_src/bad_module/some.py', 'from.import x\n', 'from unfixed_src.bad_module import x\n'),
    ('unfixed_src/bad_module/some.py', '    from . import x\n', '    from unfixed_src.bad_module import x\n'),
    ('unfixed_src/bad_module/some.py', '    from .. import x\n', '    from unfixed_src import x\n'),
    ('unfixed_src/bad_module/some.py', '    from ..foo import x\n', '    from unfixed_src.foo import x\n'),
    ('unfixed_src/bad_module/some.py', '    from.import x\n', '    from unfixed_src.bad_module import x\n'),
    ('unfixed_src/bad.py', 'from .foo import x\n', 'from unfixed_src.foo import x\n'),
    ('unfixed_src/bad.py', 'from.foo import x\n', 'from unfixed_src.foo import x\n'),
))
def test_fix(file, line, fixed):
    assert force_absolute_imports.fix(Path(file), line) == fixed
