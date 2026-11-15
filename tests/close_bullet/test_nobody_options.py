"""اختبارات Phone / Options / FakeInfo / Randoms / Status — بدون شبكة."""


def test_phone_parsing(cb_env):
    from close_bullet import Phone

    p = Phone("972567108204")
    assert p.prefix == 972
    assert str(p.local).isdigit()
    assert p.full.startswith("+")


def test_options_parse_text(cb_env):
    from close_bullet import Options

    text = 'href="https://x.com?v=abc&k=def&co=ghi"'
    assert Options.parse_text(text, "v=", "&") == "abc"
    assert Options.parse_text(text, "k=", "&") == "def"


def test_options_header_parse(cb_env):
    from close_bullet import Options

    raw = "Host: example.com\nAccept: application/json\n"
    h = Options.header_parse(raw, lower=True)
    assert h["host"] == "example.com"


def test_options_payload_parse(cb_env):
    from close_bullet import Options

    p = Options.payload_parse("a=1&b=2")
    assert p["a"] == "1" and p["b"] == "2"


def test_fake_info_shape(cb_env):
    from close_bullet import FakeInfo

    f = FakeInfo()
    assert f.first and f.last and f.full
    assert "@" in f.email
    assert len(f.password) == 15


def test_randoms_strings(cb_env):
    from close_bullet import Randoms
    import string

    s = Randoms.strings(12, string.ascii_lowercase)
    assert len(s) == 12 and s.islower()


def test_status_check_bad_retry_limit(cb_env):
    from close_bullet import status

    status.valid = 0
    status.invalid = 0
    status.retry = []
    status.Bad_to_file = []

    num = "999000111"
    for _ in range(5):
        status.append_retry(num)
    assert status.check_bad(num) == 1
    assert num in status.Bad_to_file