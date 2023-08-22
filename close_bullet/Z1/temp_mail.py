import time
from .library import Requests
from .options import Options
from .. import userdata



class Onesecmail:
    def __init__(self, Proxy=True):
        self.req = Requests().proxy_session(Proxy=Proxy)
        self.op = Options()
        self.domain = self.get_domain()
    @staticmethod
    def get_domain():
        domain_list = Requests().proxy_session().get('https://www.1secmail.com/api/v1/?action=getDomainList').json()
        domain = Options.random_from_list(domain_list)
        return domain
    def make_email(self, full_name:str) ->str:
        _ = self.op.random_from_list(['_','.','','0','1','2','3','4','5','6','7','8','9'])
        login = full_name.replace(' ', _).lower()
        return login + '@' + self.domain
    def get_message_id(self, email:str) ->list:
        login, domain = email.split("@")
        return self.req.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}').json()

    def read_message(self, email:str, message_id:int) ->dict:
        login, domain = email.split("@")
        message_body = self.req.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}')
        return message_body.json()

    def get_auto_otp(self, email:str, before:str, after:str, timeout=10) ->str:
        counter = 0
        while timeout > counter:
            try:
                time.sleep(1)
                message_id = self.get_message_id(email)[0]['id']
                message_body = self.read_message(email,message_id)['htmlBody']
                counter += 1
                otp = Options.parse_text(str(message_body),before,after)
                return otp.strip().rstrip()
            except:
                continue



