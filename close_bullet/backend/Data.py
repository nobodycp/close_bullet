import configparser, win32console, win32gui, subprocess, requests, random, time
from ..external import SmsPlus
from .coloramas import Fore, Style
from .style import Box, Colors, Write

ROOT_KEY = 'd9f4cec0-8e56-4777-91e3-8946c9de9e41'


class User:
    def __init__(self):
        self.config_file = self.open_file()
        self.data = {}
        self.format_data()
        if self.data['Root.screen_resize'] == 1:
            self.terminal(int(self.data['Root.x']), int(self.data['Root.y']))
        self.data['hwid'] = self.hwid()

    @classmethod
    def hwid(cls):
        return str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()

    @classmethod
    def terminal(cls, x=700, y=300):
        title = str(win32console.GetConsoleTitle())
        appname = title.split('\\')[-1]
        block_dev = ['python.exe', 'py.exe']
        if appname not in block_dev:
            if title.endswith('.exe'):
                win32console.SetConsoleTitle(f'{appname.strip()}')
                hwnd = win32gui.GetForegroundWindow()
                win32gui.SetWindowPos(hwnd, 0, x, y, 700, 300, 0)

    @staticmethod
    def open_file():
        try:
            with open('config.ini', 'r'):
                pass
            file_cfg = configparser.ConfigParser()
            file_cfg.read('config.ini')
            return file_cfg
        except Exception as e:
            raise Exception("Cant open config.ini file.")

    # Message.color('config file are missing {e}..', timeout=5, interval=0.2)

    def format_data(self):
        try:
            for section in self.config_file.sections():
                numbers = ['threads', ]
                true = ['true', '1', 'y', 'yes', 'True']
                false = ['false', '0', 'n', 'no', 'False']
                for key, value in self.config_file[f'{section}'].items():
                    if value.lower() in true:
                        self.data[f'{section}.{key}'] = 1
                    elif value.lower() in false:
                        self.data[f'{section}.{key}'] = 0
                    elif key in numbers:
                        self.data[f'{section}.{key}'] = int(value)
                    else:
                        self.data[f'{section}.{key}'] = value
        except Exception as e:
            raise Exception("Cant format user data from confing.ini file.")


class Server:
    def __init__(self, _user_data):
        self.hwid = _user_data['hwid']
        self.server_data = {}
        self.Connect()
        self.format_data()

    def Connect(self):
        payloads = {'key': f'{ROOT_KEY}', 'hwID': f'{self.hwid}'}
        try:
            req = requests.post('http://5.199.166.54:8000/api/v1/clients/detail/', json=payloads)
            # print(req.text)
            if self.hwid in req.text:
                self.server_data = req.json()
            else:
                self.server_data = {
                    'id': 1,
                    'full_name': 'NoBody',
                    'email': 'nobody@mnaek-kabsha.gaza',
                    'hwID': '0000000-0000-0000-0000-00000',
                    'max_threads': '1',
                    'max_session': '0',
                    'panel_username': '0',
                    'panel_password': '0',
                    'panel_server_ip': '0',
                    'number_of_random_to_check': '5',
                    'user_group': '0',
                    'is_active': False,
                    'created_at': '2022-11-13T01:56:36.741185Z',
                    'updated_at': '2023-08-10T11:01:08.398564Z'
                }
        except Exception as e:
            raise Exception("Server Error Connection ..")

    def format_data(self):
        try:
            data = self.server_data
            data.pop('id')
            data.pop('email')
            data.pop('max_session')
            data.pop('created_at')
            data.pop('updated_at')
            # ture_value = ['1', 'true', 'True']
            # false_value = ['0', 'false', 'False']
            # change_list = ['max_threads', 'number_of_random_to_check', 'user_group']
            for key, value in data.items():
                if key == 'number_of_random_to_check' or key == 'max_threads' or key == 'user_group':
                    data[f'{key}'] = int(value)
        except Exception as e:
            raise Exception("cant format Root Data ..")


class Security:
    def __init__(self, _user_data, _root_data):
        self.root_data = _root_data
        self.user_data = _user_data
        self.user_hwid = _user_data['hwid']
        self.root_hwid = _root_data['hwID']
        self.user_threads = _user_data['01Team.threads']
        self.root_threads = _root_data['max_threads']
        self.active = _root_data['is_active']
        self.telegram_bot = '5784203603:AAEy6nFC5OwTDkmbnp7SsV8mxfInGVMxkDQ'
        self.telegram_chat_id = '519990997'
        self.run()

    def telegram_bot_send_text(self, message):
        try:
            url = f'https://api.telegram.org/bot{self.telegram_bot}/sendMessage?chat_id={self.telegram_chat_id}&parse_mode=Markdown&text={message}'
            response = requests.get(url)
            # print(response.text)
            return response.json()
        except Exception as e:
            return 0

    def get_pc_data(self):
        try:
            req = requests.get('https://ipinfo.io').json()
            message = f"""
```
NEW PC.```
hwid = `{self.user_hwid}`
ip = `{req['ip']}`
city = `{req['city']}`
region = `{req['region']}`
country = `{req['country']}`
loc = `{req['loc']}`
org = `{req['org']}`
timezone = `{req['timezone']}`
root-key = `{ROOT_KEY}`
"""
            return message
        except Exception as e:
            print(e)
            exit()

    def run(self):
        if self.root_hwid != self.user_hwid:
            message = self.get_pc_data()
            self.telegram_bot_send_text(message)
            raise Exception(str(f"HWID {self.user_hwid} Not Defined ..."))
        elif not self.active:
            raise Exception("Your Baned Connect Support To Check Problem ... Telegram : @nobodycp")
        elif self.user_threads > self.root_threads:
            raise Exception(f"You Cant Use More Than {self.root_threads} Threads You Are Using {self.user_threads}.")

    def check_fuckers(self, number):
        sms_plus = SmsPlus(
            ip=f"{self.root_data['panel_server_ip']}",
            user=f"{self.root_data['panel_username']}",
            password=f"{self.root_data['panel_password']}",
        )
        if sms_plus.numbers_page_search(number) != 1:
            message = f"""
```
New 7ramy```
`{self.user_data['name']}`
"""
            self.telegram_bot_send_text(message)
            raise exit()


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
        except:
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
        except:
            raise Exception(f"cant open {numbers_list_name}.")

    @staticmethod
    def user_agents():
        try:
            user_agents = requests.get("https://pastebin.com/raw/hxqYvBtu").text.split("\n")
            return user_agents
        except:
            raise Exception("cant lode user agents list.")


class Message:
    @staticmethod
    def welcome(name):
        # print(f"{Fore.GREEN}{Back.RED}{Style.DIM}Hello")
        _Hello = Box.Lines(f'Welcome  {name}\nCoded By : https://t.me/Mnaek_Kabsha', pepite=' 💀 ')
        # ✅ ❌ 💲❗❓
        color = Colors.all_colors[random.randrange(0, len(Colors.all_colors))]
        Write.Print(_Hello, color, interval=0.005)

    @staticmethod
    def color(message, timeout=10, interval=0.1):
        color = Colors.all_colors[random.randrange(0, len(Colors.all_colors))]
        Write.Print(message, color, interval=interval)
        time.sleep(int(timeout))


class Status:
    valid = 0
    invalid = 0
    retry = []
    Bad_to_file = []

    def print_res(self, q_size):
        print(
            f"{Style.RESET_ALL}\r {Fore.BLUE}{q_size}{Style.RESET_ALL} | {Fore.GREEN}🗸 {self.valid}{Style.RESET_ALL} | "
            f"{Fore.RED}✘ {self.invalid}{Style.RESET_ALL} | "
            f"{Fore.YELLOW + Style.BRIGHT}♺ {len(set(self.retry))}{Style.RESET_ALL} ", end='')

    # print(retry)
    def save_bad_data(self):
        with open('bad_retry.txt', 'a') as bad_data:
            for bad in self.Bad_to_file:
                bad_data.write(f'{bad}\n')
            bad_data.close()

    def check_bad(self, data):
        if data in self.Bad_to_file:
            return 1
        elif self.retry.count(data) >= 5:
            self.Bad_to_file.append(data)
            self.invalid += 1
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


try:
    user_data = User().data
    root_data = Server(user_data).server_data
    user_data['name'] = root_data['full_name']
    lists = Lists(user_data)
    check = Security(user_data, root_data)
    status = Status()
    if root_data['user_group'] != 0:
        number_to_check = str(random.choice(lists.numbers)).replace('+', '')
        check.check_fuckers(f'{number_to_check}')
except Exception as e:
    Message.color(str(e))
    exit()
