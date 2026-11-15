import random

import requests

_USER_AGENTS_CACHE = None


class Lists:
    def __init__(self, userdata):
        self.user_data = userdata
        self.numbers = self.numbers()
        self.proxys = self.proxys()
        self.user_agents = self.user_agents()

    def proxys(self):
        proxy_list_name = self.user_data['Proxy.list']
        try:
            with open(proxy_list_name) as proxy_list:
                proxylist = proxy_list.readlines()
            return proxylist
        except Exception:
            raise Exception(f"cant open {proxy_list_name}.")

    def numbers(self):
        numbers_list_name = self.user_data['Number.list']
        number_list_randomize = self.user_data['Number.list.randomize']
        try:
            with open(numbers_list_name) as numbers_list:
                numbers_list = numbers_list.readlines()
                if number_list_randomize:
                    numbers_list = random.sample(numbers_list, len(numbers_list))
                    return list(map(lambda s: s.strip(), numbers_list))
                else:
                    return list(map(lambda s: s.strip(), numbers_list))
        except Exception:
            raise Exception(f"cant open {numbers_list_name}.")

    @staticmethod
    def user_agents():
        global _USER_AGENTS_CACHE
        if _USER_AGENTS_CACHE is not None:
            return _USER_AGENTS_CACHE
        try:
            _USER_AGENTS_CACHE = requests.get(
                "https://pastebin.com/raw/hxqYvBtu", timeout=15
            ).text.split("\n")
        except Exception:
            _USER_AGENTS_CACHE = {"", ""}
        return _USER_AGENTS_CACHE