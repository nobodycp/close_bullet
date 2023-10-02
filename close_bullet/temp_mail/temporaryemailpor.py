import time, re
from .. import Requests


class TemporaryEmailPor:
    s = Requests.proxy_session(Proxy=True)

    def __init__(self, text_from_message: str, timeout: int = 20):
        self.token = None
        self.email: str = self.get_email()
        self.text_from_message: str = text_from_message
        self.timeout: int = timeout

    def get_email(self):
        headers = {
            'Host': 'mob2.temp-mail.org',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': '3.33',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        while True:
            try:
                get_email = self.s.post('https://mob2.temp-mail.org/mailbox', headers=headers, json={})
                # print(get_email)
                self.token = str(get_email.json()['token']).strip()
                return get_email.json()['mailbox']
            except Exception as e:
                continue

    def get_message(self):
        headers = {
            'host': 'mob2.temp-mail.org',
            'accept': 'application/json',
            'accept-Encoding': 'gzip, deflate',
            'user-agent': '3.33',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'{self.token}',
        }
        try:
            for _ in range(int(self.timeout / 3)):
                time.sleep(3)
                res = self.s.get('https://mob2.temp-mail.org/messages', headers=headers)
                # print(res.text)
                for message in res.json()['messages']:
                    if f'{self.text_from_message}' in str(message):
                        messages_id = message['_id']
                        res = self.s.get(f'https://mob2.temp-mail.org/messages/{messages_id}', headers=headers)
                        return res.json()
        except Exception as e:
            pass

    def otp(self, length):
        try:
            message = self.get_message()['bodyHtml']
            pattern = '(\d{' + str(length) + '})'
            matches = re.findall(pattern, str({message}))
            if len(matches) >= 1:
                return matches
            else:
                raise Exception('Cant Get Otp.')
        except:
            raise Exception('Cant Get Otp.')

    def link(self):
        try:
            message = self.get_message()['bodyHtml']
            pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
            urls = re.findall(pattern, message)
            # print(urls)
            if len(urls) >= 1:
                return urls
            else:
                raise Exception('Cant Get email links.')
        except:
            raise Exception('Cant Get email links.')
