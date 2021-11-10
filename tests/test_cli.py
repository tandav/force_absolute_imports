import sys
import subprocess


def test_arguments_passed():
    cmd = sys.executable, '-m', 'force_absolute_imports'
    p = subprocess.run(cmd, text=True)
    assert p.returncode == 2
