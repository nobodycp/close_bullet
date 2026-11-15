"""تشغيل متوازٍ لقائمة أرقام مع إعادة محاولة آمنة للثريدات."""

import concurrent.futures
import logging
import threading
from typing import Callable, Iterable, Optional

SendFn = Callable[[str], int]


def run_batch(
    send_fn: SendFn,
    numbers: Iterable[str],
    userdata: dict,
    status,
    message_cls,
    *,
    welcome: bool = True,
    done_message: str = "All Tasks Done !!",
) -> None:
    numbers = list(numbers)
    if welcome:
        message_cls.welcome(userdata["name"])

    remaining_lock = threading.Lock()
    remaining = len(numbers)
    retry_queue: list = []
    retry_lock = threading.Lock()

    def schedule_retry(item: str) -> None:
        with retry_lock:
            retry_queue.append(item)

    def worker(item: str) -> None:
        nonlocal remaining
        with remaining_lock:
            remaining -= 1
            left = remaining
        status.print_res(left)

        if status.check_bad(item) == 1 or item in status.Bad_to_file:
            return

        try:
            task = send_fn(item)
            if task == 1:
                status.add_valid()
            elif task == 0:
                status.add_invalid()
            elif task == 2:
                if userdata.get("01Team.retry_failed"):
                    status.append_retry(item)
                    if status.check_bad(item) != 1:
                        schedule_retry(item)
                else:
                    status.add_invalid()
        except Exception as e:
            print(f"Error sending item: {e}")
            logging.error("Error sending item: %s", e)

    max_workers = int(userdata["01Team.threads"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker, n) for n in numbers]
        concurrent.futures.wait(futures)

        while retry_queue:
            batch: list = []
            with retry_lock:
                batch, retry_queue = retry_queue[:], []
            if not batch:
                break
            retry_futures = [executor.submit(worker, item) for item in batch]
            concurrent.futures.wait(retry_futures)

    print(f"\n{done_message}")