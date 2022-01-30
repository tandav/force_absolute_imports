import shutil
import subprocess
import sys
from pathlib import Path

import pytest

import force_absolute_imports


def test_only_py_files():
    with pytest.raises(SystemExit) as e:
        force_absolute_imports.only_absolute_file('file.java')
        assert e.value.code == 2


def test_exit_code_0():
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'unfixed_src/good.py')).returncode == 0
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'unfixed_src/good_module')).returncode == 0


def test_exit_code_1():
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'unfixed_src/bad.py')).returncode == 1
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'unfixed_src/bad_module')).returncode == 1


def test_exit_code_2():
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports')).returncode == 2
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'file.java')).returncode == 2
    assert subprocess.run((sys.executable, '-m', 'force_absolute_imports', 'gkjslf')).returncode == 2


@pytest.fixture
def source_dir():
    dst = Path('unfixed_src2')
    shutil.copytree('unfixed_src', dst)
    yield dst
    shutil.rmtree(dst)


def test_fix_inplace(source_dir):
    subprocess.run((sys.executable, '-m', 'force_absolute_imports', '--in-place', source_dir))
    assert force_absolute_imports.only_absolute_folder(source_dir)
