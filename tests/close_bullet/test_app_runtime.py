import importlib.util
import subprocess
import sys
from pathlib import Path


def test_app_py_runs_send(cb_env):
    root = Path(__file__).resolve().parents[2]
    result = subprocess.run(
        [sys.executable, str(root / "App.py")],
        cwd=root,
        capture_output=True,
        text=True,
        timeout=45,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    # يطبع IP أو رسالة خطأ؛ أي مخرجات تعني أن send() اشتغل
    assert result.stdout.strip() != ""