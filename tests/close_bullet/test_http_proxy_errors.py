import requests


def test_friendly_407_message(cb_env):
    from close_bullet.nobody.http_errors import friendly_http_error

    err = requests.exceptions.ProxyError(
        "HTTPSConnectionPool(host='x', port=443): Max retries exceeded",
        response=None,
    )
    err.__cause__ = OSError("Tunnel connection failed: 407 Proxy Authentication Required")
    msg = str(friendly_http_error(err))
    assert "[Proxy]" in msg
    assert "407" in msg
    assert "active = 0" in msg


def test_wrap_session_reraises_clear_message(cb_env):
    from close_bullet.nobody.http_errors import wrap_session_request

    s = requests.Session()

    def broken(method, url, **kwargs):
        e = requests.exceptions.ProxyError("max retries", response=None)
        e.__cause__ = OSError("Tunnel connection failed: 407 Proxy Authentication Required")
        raise e

    s.request = broken  # type: ignore[method-assign]
    wrap_session_request(s)
    try:
        s.request("GET", "https://ipinfo.io/")
    except Exception as e:
        assert "[Proxy]" in str(e) and "407" in str(e)
        assert "Authentication failed" in str(e)
        return
    raise AssertionError("expected clear proxy error")