from unittest.mock import MagicMock


def test_run_batch_counts(cb_env):
    from close_bullet.backend.core.runner import run_batch
    from close_bullet import status, userdata
    from close_bullet.backend.core.message import Message

    status.valid = 0
    status.invalid = 0
    status.retry = []
    status.Bad_to_file = []

    def send_ok(n):
        return 1 if n.endswith("4") else 0

    run_batch(
        send_ok,
        ["111", "224"],
        userdata,
        status,
        Message,
        welcome=False,
        done_message="done",
    )
    assert status.valid == 1
    assert status.invalid == 1