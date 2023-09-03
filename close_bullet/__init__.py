################### System Area #########################
import random
import time
import base64
import string
import queue
que = queue.Queue()
##################### Dev Area ##########################
from .Z1 import Message, ResBar, userdata, lists
#-------------------------------------------------------#
from .Z1.options import Randoms, Option, FakeName, Phone
#-------------------------------------------------------#
from .Z1.captcha import Nopecha, OneStCaptcha
#-------------------------------------------------------#
from .Z1.library import Requests
#-------------------------------------------------------#
try:
    from .Z1 import Onesecmail
    temp_1secmail = Onesecmail()
except Exception as e:
    # print(str(e))
    temp_1secmail = 0
    pass

#################### Customs Area #######################
res_bar = ResBar()
cp_Nopecha = Nopecha()
cp_1stcaptcha = OneStCaptcha()




#################### Controls Area ######################
def que_put_one():
    for data in lists.number:
        que.put(data)

def que_put_many(lst,chunk_size=5):
    def read_in_chunks():
        for i in range(0,len(lst),chunk_size):
            yield lst[i:i + chunk_size]

    for data in read_in_chunks():
        que.put(data)

def testtest():
    print("Test")