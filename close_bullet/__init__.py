import os
from .backend import Message, status, lists, user_data as userdata
from .nobody import Randoms, Options, FakeInfo, Phone, Requests

temp_folder = os.path.expanduser("~/Desktop/Nobody_temp/")
if not os.path.exists(temp_folder):
    os.mkdir(temp_folder)






# def que_put_many(lst,chunk_size=5):
#     def read_in_chunks():
#         for i in range(0,len(lst),chunk_size):
#             yield lst[i:i + chunk_size]
#
#     for data in read_in_chunks():
#         que.put(data)

