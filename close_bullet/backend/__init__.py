from .Data import Data
from .security import Check
from .general import *


try:
    config = Data()
    config.run()
    userdata = config.user_data
    backend_data = config.backend_data
    Check(backend_data).run()
except Exception as e:
    Message.color(str(e))
    exit()

