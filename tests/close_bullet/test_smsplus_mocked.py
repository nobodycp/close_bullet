from unittest.mock import MagicMock, patch


def test_smsplus_numbers_page_search_found(cb_env):
    from close_bullet.external.smsplus import SmsPlus

    client = SmsPlus.__new__(SmsPlus)
    client.ip = "167.99.35.211"
    client.ua = "test-agent"
    client.s = MagicMock()
    mock_resp = MagicMock()
    mock_resp.text = '{"listcount":1,"data":[]}'
    client.s.post.return_value = mock_resp
    assert client.numbers_page_search("123") == 1


@patch.object(__import__("close_bullet.external.smsplus", fromlist=["SmsPlus"]).SmsPlus, "login", return_value=1)
def test_smsplus_login_ok(_login, cb_env):
    from close_bullet.external.smsplus import SmsPlus

    with patch("close_bullet.external.smsplus.requests.session") as sess:
        mock_s = MagicMock()
        sess.return_value = mock_s
        mock_resp = MagicMock()
        mock_resp.text = '"status":"ok"'
        mock_s.post.return_value = mock_resp
        client = SmsPlus("1.2.3.4", "u", "p")
        assert client.s is mock_s