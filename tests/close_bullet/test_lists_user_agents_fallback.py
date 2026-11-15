from unittest.mock import patch


def test_lists_user_agents_fallback(cb_env):
    from close_bullet.backend.core import lists as lists_mod
    from close_bullet.backend.core.lists import Lists

    lists_mod._USER_AGENTS_CACHE = None
    with patch("close_bullet.backend.core.lists.requests.get", side_effect=OSError("offline")):
        ua = Lists.user_agents()
    assert "" in ua or len(ua) >= 1
    lists_mod._USER_AGENTS_CACHE = None