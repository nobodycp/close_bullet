"""اختبارات التحميل الأولي — نفس سلوك import close_bullet في App.py و Run.py."""


def test_import_exports(cb_env):
    import close_bullet as cb

    assert cb.userdata is not None
    assert cb.lists is not None
    assert cb.status is not None
    assert cb.Requests is not None
    assert cb.Phone is not None
    assert cb.temp_folder.endswith("Nobody_temp/")


def test_offline_mode(cb_env):
    import close_bullet as cb

    assert cb.userdata.get("Local.offline_mode") == 1
    assert cb.userdata.get("name")


def test_lists_loaded(cb_env):
    import close_bullet as cb

    assert len(cb.lists.numbers) >= 1
    assert len(cb.lists.proxys) >= 1


def test_runpy_contract(cb_env):
    """ما يحتاجه Run.py من الحالة العامة."""
    import close_bullet as cb

    assert "01Team.threads" in cb.userdata
    assert hasattr(cb.status, "valid")
    assert hasattr(cb.status, "check_bad")
    assert cb.status.check_bad("not-in-retry") == 0