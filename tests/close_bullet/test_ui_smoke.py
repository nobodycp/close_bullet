def test_message_color_no_crash(cb_env, monkeypatch):
    from close_bullet.backend.core.message import Message

    monkeypatch.setattr("close_bullet.backend.core.message.time.sleep", lambda *_: None)
    Message.color("smoke", timeout=0, interval=0)


def test_status_print_res(cb_env, capsys):
    from close_bullet.backend.core.status import Status

    s = Status()
    s.valid = 1
    s.print_res(10)
    out = capsys.readouterr().out
    assert "1" in out