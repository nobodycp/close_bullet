from unittest.mock import MagicMock, patch


def test_onesecmail_make_email(cb_env):
    from close_bullet.temp_mail.onesecmail import Onesecmail

    with patch.object(Onesecmail, "domain_list", return_value=["1secmail.com"]):
        mail = Onesecmail("John Doe", "verify", timeout=3)
        assert "@" in mail.email
        assert "john" in mail.email.lower() and "1secmail.com" in mail.email


def test_timetech_base64_roundtrip(cb_env):
    from close_bullet.temp_mail.timetech import TimeTech

    assert TimeTech.base64_decode(TimeTech.base64_encode("hello")) == "hello"