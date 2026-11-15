def test_runpy_imports(cb_env):
    import importlib.util
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location("run_module", root / "Run.py")
    module = importlib.util.module_from_spec(spec)
    # تحميل التبعيات فقط: اختبار أن close_bullet جاهز لما يستدعيه Run
    import close_bullet

    assert close_bullet.userdata.get("01Team.threads") >= 1
    assert len(close_bullet.lists.numbers) >= 1
    assert spec.loader is not None