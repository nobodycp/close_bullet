from .Data import Data
from .general import *
from .security import Check


try:
    config = Data()
    config.run()
    userdata = config.user_data
    backend_data = config.backend_data
    Lists = Lists(userdata)
    Check(backend_data).run()
except Exception as e:
    General.error_message(str(e))
    exit()
