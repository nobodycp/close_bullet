from .backend import General,ProcessBar,userdata, Lists
from .Z1 import Options,Requests,userdata,Nopecha,OneStCaptcha
import time
import random
from threading import Thread
from queue import Queue

process = ProcessBar()
captcha1 = OneStCaptcha()
captcha2 = Nopecha
que = Queue()

def que_put_one():
    for data in Lists.number:
        que.put(data)

def que_put_many(lst,chunk_size=5):
    def read_in_chunks():
        for i in range(0,len(lst),chunk_size):
            yield lst[i:i + chunk_size]

    for data in read_in_chunks():
        que.put(data)

