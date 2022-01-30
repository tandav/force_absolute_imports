from pathlib import Path

import pytest

import force_absolute_imports


@pytest.mark.parametrize('line, result', (
    ('from . import x', {'s0': '', 's1': ' ', 'dots': '.', 's2': ' ', 'rest': 'import x'}),
    ('from .. import x', {'s0': '', 's1': ' ', 'dots': '..', 's2': ' ', 'rest': 'import x'}),
    ('from .foo import x', {'s0': '', 's1': ' ', 'dots': '.', 's2': '', 'rest': 'foo import x'}),
    ('from.foo import x', {'s0': '', 's1': '', 'dots': '.', 's2': '', 'rest': 'foo import x'}),
    ('from .foo.bar import x', {'s0': '', 's1': ' ', 'dots': '.', 's2': '', 'rest': 'foo.bar import x'}),
    ('from ..foo.bar import x', {'s0': '', 's1': ' ', 'dots': '..', 's2': '', 'rest': 'foo.bar import x'} ),
    ('    from .. import x', {'s0': '    ', 's1': ' ', 'dots': '..', 's2': ' ', 'rest': 'import x'}),
))
def test_parse(line, result):
    assert force_absolute_imports.parse(line) == result


@pytest.mark.parametrize('file, line, fixed', (
    ('unfixed_src/bad_module/some.py', 'from . import x', 'from unfixed_src.bad_module import x'),
    ('unfixed_src/bad_module/some.py', 'from .. import x', 'from unfixed_src import x'),
    ('unfixed_src/bad_module/some.py', 'from ..foo import x', 'from unfixed_src.foo import x'),
    ('unfixed_src/bad_module/some.py', 'from.import x', 'from unfixed_src.bad_module import x'),
    ('unfixed_src/bad_module/some.py', '    from . import x', '    from unfixed_src.bad_module import x'),
    ('unfixed_src/bad_module/some.py', '    from .. import x', '    from unfixed_src import x'),
    ('unfixed_src/bad_module/some.py', '    from ..foo import x', '    from unfixed_src.foo import x'),
    ('unfixed_src/bad_module/some.py', '    from.import x', '    from unfixed_src.bad_module import x'),
    ('unfixed_src/bad.py', 'from .foo import x', 'from unfixed_src.foo import x'),
    ('unfixed_src/bad.py', 'from.foo import x', 'from unfixed_src.foo import x'),
))
def test_fix(file, line, fixed):
    assert force_absolute_imports.fix(Path(file), line) == fixed
