"""اختبارات User.format_data منفصلة عن الشبكة."""


def test_user_format_data_boolean_and_int(cb_env):
    from close_bullet.backend.Data import User

    u = User()
    assert u.data["Proxy.active"] in (0, 1)
    assert isinstance(u.data["01Team.threads"], int)
    assert "hwid" in u.data and len(u.data["hwid"]) > 0