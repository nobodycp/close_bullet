from close_bullet.backend import General, ProcessBar
from close_bullet.Z1 import Options, Requests, userdata, Lists, Nopecha, OneStCaptcha

process = ProcessBar()
captcha1 = OneStCaptcha()
captcha2 = Nopecha


# def quee_put_one():
#     for data in Lists.number: # type: ignore
#         que.put_nowait(data)

# def quee_put_many(chunk_size=5):
#     lst = Lists.number # type: ignore
#     def read_in_chunks():
#         for i in range(0, len(lst), chunk_size):
#             yield lst[i:i + chunk_size]
#     for data in read_in_chunks():
#         que.put(data)
