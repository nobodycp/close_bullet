import random

from close_bullet.backend.core import Lists, Message, Status
from close_bullet.backend.core.config_user import User
from close_bullet.backend.core.security import Security
from close_bullet.backend.core.server_client import Server

user_data = None
root_data = None
lists = None
check = None
status = None

try:
    user_data = User().data
    root_data = Server(user_data).server_data
    user_data["name"] = root_data["full_name"]
    lists = Lists(user_data)
    check = Security(user_data, root_data)
    status = Status()
    if root_data["user_group"] != 0:
        number_to_check = str(random.choice(lists.numbers)).replace("+", "")
        check.check_fuckers(f"{number_to_check}")
except Exception as e:
    Message.color(str(e), timeout=2, interval=0.05)
    exit()