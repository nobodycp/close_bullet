import random
import time
import requests
from ..global_lib import *

user_agents = requests.get("https://pastebin.com/raw/hxqYvBtu").text.split("\n")

class Lists:
    def __init__(self, userdata):
        self.user_data = userdata
        self.proxy = self._proxy()
        self.number = self._number()

    def _proxy(self):
        try:
            with open(str(self.user_data['Proxy.list'])) as proxylist:
                # print("Open proxy")
                proxylist = proxylist.readlines()
            return proxylist
        except Exception as e:
            raise Exception(f"proxy.txt Have error ---> {e}")

    def _number(self):
        try:
            with open(self.user_data['Number.list']) as list_:
                list_ = list_.readlines()
                if self.user_data['Number.list.randomize']:
                    list_ = random.sample(list_,len(list_))
                    return list(map(lambda s:s.strip(),list_))
                else:
                    return list(map(lambda s:s.strip(),list_))
        except Exception as e:
            raise e

    @staticmethod
    def user_agents():
        return user_agents


class General:
    def __init__(self, userdata):
        self.user_data = userdata
    @staticmethod
    def welcome_message(name):
        # print(f"{Fore.GREEN}{Back.RED}{Style.DIM}Hello")
        _Hello = Box.Lines(f'Welcome ⚡ {name}\nCoded By : https://t.me/Mnaek_Kabsha',pepite=' 💀 ')
        # ✅ ❌ 💲❗❓
        color = Colors.all_colors[random.randrange(0,len(Colors.all_colors))]
        Write.Print(_Hello,color,interval=0.01)

    @staticmethod
    def error_message(message,timeout=10, interval=0.1):
        color = Colors.all_colors[random.randrange(0,len(Colors.all_colors))]
        Write.Print(message ,color,interval=interval)
        time.sleep(int(timeout))


class ProcessBar:
    Successfully = 0
    Retry = []
    Failed = 0
    Bad = []

    def print_res(self,q_size):
        # print(f"This is {Fore.GREEN}color{Style.RESET_ALL}!")
        print(
            f"{Style.RESET_ALL}\r {Fore.BLUE}{q_size}{Style.RESET_ALL} | {Fore.GREEN}🗸 {self.Successfully}{Style.RESET_ALL} | "
            f"{Fore.RED}✘ {self.Failed}{Style.RESET_ALL} | "
            f"{Fore.YELLOW + Style.BRIGHT}♺ {len(set(self.Retry))}{Style.RESET_ALL} ",end='')
        # print(retry)

    def save_bad_data(self):
        with open('bad_retry.txt','a') as bad_data:
            for bad in self.Bad:
                bad_data.write(f'{bad}\n')
            bad_data.close()

    def check_bad(self,data):
        if data in self.Bad:
            return 1
        elif self.Retry.count(data) >= 5:
            self.Bad.append(data)
            self.Failed += 1
            try:
                self.Retry.remove(data)
                self.Retry.remove(data)
                self.Retry.remove(data)
                self.Retry.remove(data)
                self.Retry.remove(data)
            except:
                pass
            return 1
        else:
            return 0


