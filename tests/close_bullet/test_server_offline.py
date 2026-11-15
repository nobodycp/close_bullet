def test_server_offline_profile(cb_env):
    from close_bullet.backend.Data import Server, User

    user = User()
    server = Server(user.data)
    assert server.server_data["is_active"] is True
    assert server.server_data["hwID"] == user.data["hwid"]
    assert server.server_data["max_threads"] == 500