import requests

from close_bullet.backend.constants import ROOT_KEY
from close_bullet.external import SmsPlus


class Security:
    def __init__(self, _user_data, _root_data):
        self.root_data = _root_data
        self.user_data = _user_data
        self.user_hwid = _user_data["hwid"]
        self.root_hwid = _root_data["hwID"]
        self.user_threads = _user_data["01Team.threads"]
        self.root_threads = _root_data["max_threads"]
        self.active = _root_data["is_active"]
        self.telegram_bot = "5784203603:AAEy6nFC5OwTDkmbnp7SsV8mxfInGVMxkDQ"
        self.telegram_chat_id = "519990997"
        self.run()

    def telegram_bot_send_text(self, message):
        try:
            url = (
                f"https://api.telegram.org/bot{self.telegram_bot}/sendMessage"
                f"?chat_id={self.telegram_chat_id}&parse_mode=Markdown&text={message}"
            )
            response = requests.get(url)
            return response.json()
        except Exception:
            return 0

    def get_pc_data(self):
        try:
            req = requests.get("https://ipinfo.io").json()
            return f"""
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
        except Exception as e:
            print(e)
            exit()

    def run(self):
        if self.root_hwid != self.user_hwid:
            message = self.get_pc_data()
            self.telegram_bot_send_text(message)
            raise Exception(str(f"HWID {self.user_hwid} Not Defined ..."))
        if not self.active:
            raise Exception(
                "Your Baned Connect Support To Check Problem ... Telegram : @nobodycp"
            )
        if self.user_threads > self.root_threads:
            raise Exception(
                f"You Cant Use More Than {self.root_threads} Threads You Are Using {self.user_threads}."
            )

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