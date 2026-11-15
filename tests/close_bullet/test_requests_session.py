"""اختبارات Requests.proxy_session — بروكسي معطّل في fixture."""


def test_proxy_session_no_proxy_when_inactive(cb_env):
    from close_bullet import Requests

    s = Requests.proxy_session()
    assert s.proxies == {}

    s_force = Requests.proxy_session(True)
    assert s_force.proxies == {}, "config active=0 must override proxy_session(True)"


def test_cloudscraper_session(cb_env):
    from close_bullet import Requests

    s = Requests.cloudscraper()
    assert s is not None