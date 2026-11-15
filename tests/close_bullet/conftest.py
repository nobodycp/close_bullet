"""إعداد بيئة الاختبار: config.ini وملفات قوائم في مجلد عمل معزول."""

from pathlib import Path
import shutil
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PACKAGES = PROJECT_ROOT / "packages" / "close_bullet"
FIXTURES = PROJECT_ROOT / "tests" / "fixtures"


@pytest.fixture(scope="session", autouse=True)
def _project_on_path():
    packages_str = str(PACKAGES)
    if packages_str not in sys.path:
        sys.path.insert(0, packages_str)


@pytest.fixture()
def cb_env(tmp_path, monkeypatch):
    """مجلد عمل يحاكي تشغيل SmsWork مع offline_mode."""
    shutil.copy(FIXTURES / "minimal_config.ini", tmp_path / "config.ini")
    (tmp_path / "numbers.txt").write_text("972567108204\n", encoding="utf-8")
    (tmp_path / "proxy.txt").write_text("127.0.0.1:8080\n", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    yield tmp_path