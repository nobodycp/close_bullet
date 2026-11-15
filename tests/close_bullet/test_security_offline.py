def test_security_passes_when_hwid_matches_offline(cb_env):
    from close_bullet.backend.Data import Security, Server, User

    user = User()
    root = Server(user.data).server_data
    # لا يرفع استثناء
    Security(user.data, root)