from .backend import General, ProcessBar, userdata
from .Z1 import Options, Requests, userdata, Lists, Nopecha, OneStCaptcha
import queue
from threading import Thread

process = ProcessBar()
captcha1 = OneStCaptcha()
captcha2 = Nopecha
que = queue.Queue()


def que_put_one():
    for data in Lists.number:
        que.put(data)
    que.join()

# def quee_put_many(chunk_size=5):
#     lst = Lists.number # type: ignore
#     def read_in_chunks():
#         for i in range(0, len(lst), chunk_size):
#             yield lst[i:i + chunk_size]
#     for data in read_in_chunks():
#         que.put(data)
