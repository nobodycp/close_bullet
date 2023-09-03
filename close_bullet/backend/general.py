import random
import time
import requests
from .coloramas import Fore, Style
from .style import Box, Colors, Write


user_agents = requests.get("https://pastebin.com/raw/hxqYvBtu").text.split("\n")

class Lists:
    def __init__(self, userdata):
        self.user_data = userdata
        self.proxy = self._proxy()
        self.number = self._number()
        self.user_agents = self.user_agents()
    def _proxy(self):
        try:
            with open(str(self.user_data['Proxy.list'])) as proxylist:
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


class Message:
    @staticmethod
    def welcome(name):
        # print(f"{Fore.GREEN}{Back.RED}{Style.DIM}Hello")
        _Hello = Box.Lines(f'Welcome  {name}\nCoded By : https://t.me/Mnaek_Kabsha',pepite=' 💀 ')
        # ✅ ❌ 💲❗❓
        color = Colors.all_colors[random.randrange(0,len(Colors.all_colors))]
        Write.Print(_Hello,color,interval=0.01)
    @staticmethod
    def color(message,timeout=10, interval=0.1):
        color = Colors.all_colors[random.randrange(0,len(Colors.all_colors))]
        Write.Print(message ,color,interval=interval)
        time.sleep(int(timeout))



class ResBar:
    valid = 0
    retry = []
    failed = 0
    Bad_to_file = []

    def print_res(self,q_size):
        print(
            f"{Style.RESET_ALL}\r {Fore.BLUE}{q_size}{Style.RESET_ALL} | {Fore.GREEN}🗸 {self.valid}{Style.RESET_ALL} | "
            f"{Fore.RED}✘ {self.failed}{Style.RESET_ALL} | "
            f"{Fore.YELLOW + Style.BRIGHT}♺ {len(set(self.retry))}{Style.RESET_ALL} ",end='')
        # print(retry)
    def save_bad_data(self):
        with open('bad_retry.txt','a') as bad_data:
            for bad in self.Bad_to_file:
                bad_data.write(f'{bad}\n')
            bad_data.close()

    def check_bad(self,data):
        if data in self.Bad_to_file:
            return 1
        elif self.retry.count(data) >= 5:
            self.Bad_to_file.append(data)
            self.failed += 1
            try:
                self.retry.remove(data)
                self.retry.remove(data)
                self.retry.remove(data)
                self.retry.remove(data)
                self.retry.remove(data)
            except:
                pass
            return 1
        else:
            return 0

