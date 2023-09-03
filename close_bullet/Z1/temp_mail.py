import time
from .library import Requests
from .options import Randoms, Option
req = Requests.proxy_session(Proxy=False)

class Onesecmail:
    Onesecmail_domains = req.get('https://www.1secmail.com/api/v1/?action=getDomainList').json()
    def make_email(self, full_name:str) ->str:
        _ = Randoms.from_list(['_','.','','0','1','2','3','4','5','6','7','8','9'])
        login = full_name.replace(' ', _).lower()
        return login + '@' + Randoms.from_list(self.Onesecmail_domains)
    @staticmethod
    def get_message_id(email:str) ->list:
        login,domain = email.split("@")
        return req.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}').json()
    @staticmethod
    def read_message(email:str, message_id:int) ->dict:
        login, domain = email.split("@")
        message_body = req.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}')
        return message_body.json()
    def get_auto_otp(self, email:str, before:str, after:str, timeout=10) ->str:
        counter = 0
        while timeout > counter:
            try:
                time.sleep(1)
                message_id = self.get_message_id(email)[0]['id']
                message_body = self.read_message(email,message_id)['htmlBody']
                counter += 1
                otp = Option.parse_text(str(message_body),before,after)
                return otp.strip().rstrip()
            except:
                continue

