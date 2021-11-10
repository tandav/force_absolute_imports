import sys
import subprocess

import pytest

import force_absolute_imports


def test_arguments_passed():
    cmd = sys.executable, '-m', 'force_absolute_imports'
    p = subprocess.run(cmd, text=True)
    assert p.returncode == 2


def test_only_py_files():
    with pytest.raises(SystemExit) as e:
        force_absolute_imports.only_absolute_file('file.java')
    assert e.value.code == 2
