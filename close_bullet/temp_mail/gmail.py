import re
import time

from .. import  Requests, Randoms


class Gmail:
    s = Requests.proxy_session(Proxy=True)
    domain_list = ['gmail.com', 'googlemail.com']
    # domain_list = ['hotmail.com']
    rapidapi_key = 'f871a22852mshc3ccc49e34af1e8p126682jsn734696f1f081'
    def __init__(self, text_from_message:str, timeout:int=20):
        self.timeout:int = timeout
        self.text_from_message:str = text_from_message
        self.timestamp:int = 1
        self.email:str = self.get_email()

    def get_key(self, payloads:dict):
        headers = {
            'Host': 'smailpro.com',
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'com.duckduckgo.mobile.android',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Origin': 'https://smailpro.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://smailpro.com/advanced/',
            }
        try:
            req = self.s.post('https://smailpro.com/app/key', headers=headers, json=payloads)
            if '"msg":"OK"' in req.text:
                return req.json()['items']
        except Exception as e:
            pass

    def get_email(self):
        headers = {
            'Host': 'public-w.sonjj.com',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'com.duckduckgo.mobile.android',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Sec-Fetch-Mode': 'cors',
            'X-Rapidapi-Ua': 'RapidAPI-Playground',
            'Origin': 'https://smailpro.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://smailpro.com/',
            }
        payloads = {
            "domain": Randoms.from_list(self.domain_list),
            "username":"random",
            "server":"server-1",
            "type":"alias"
            }
        try:
            req = self.s.get(f'https://public-w.sonjj.com/email/gm/get?key={self.get_key(payloads)}&rapidapi-key={self.rapidapi_key}', headers=headers)
            if '"msg":"OK"' in req.text:
                self.timestamp = req.json()['items']['timestamp']
                return req.json()['items']['email']
        except Exception as e:
            raise Exception("Cant Get Email.")

    def get_messages(self):
        headers = {
            'Host': 'public-w.sonjj.com',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'com.duckduckgo.mobile.android',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rapidapi-Ua': 'RapidAPI-Playground',
            'Origin': 'https://smailpro.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://smailpro.com/',
            }
        payloads = {
            'email':f'{self.email}',
            'timestamp':self.timestamp
            }
        try:
            for _ in range(int(self.timeout/3)):
                time.sleep(3)
                key = self.get_key(payloads)
                res = self.s.get(f'https://public-w.sonjj.com/email/gm/check?key={key}&rapidapi-key={self.rapidapi_key}&email={self.email}&timestamp={self.timestamp}',headers=headers)
                # print(res.text)
                for message in res.json()['items']:
                    if f'{str(self.text_from_message).lower()}' in str(message).lower():
                        messages_id = message['mid']
                        return messages_id

        except Exception as e:
            pass

    def read_message(self):
        payloads = {
            'email':f'{self.email}',
            'timestamp':self.timestamp
            }
        headers = {
            'Host': 'public-w.sonjj.com',
            'Accept': 'application/json, text/plain, */*',
            'X-Requested-With': 'com.duckduckgo.mobile.android',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rapidapi-Ua': 'RapidAPI-Playground',
            'Origin': 'https://smailpro.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://smailpro.com/',
            }
        message_id = self.get_messages()
        for _ in range(int(self.timeout/3)):
            key = self.get_key(payloads)
            try:
                req = self.s.get(f'https://public-w.sonjj.com/email/gm/read?key={key}&rapidapi-key={self.rapidapi_key}&email={self.email}&message_id={message_id}', headers=headers)
                return req.json()['items']

            except Exception as e:
                pass

    def otp(self, length):
        try:
            message = self.read_message()
            pattern = '(\d{' + str(length) + '})'
            matches = re.findall(pattern,str({message['body']}))
            if len(matches) >= 1:
                return matches
            else:
                raise Exception('Cant Get Otp.')
        except:
            raise Exception('Cant Get Otp.')

    def link(self):
        try:
            message = self.read_message()
            # print(message['body'])
            pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
            urls = re.findall(pattern,message['body'])
            if len(urls) >= 1:
                return urls
            else:
                raise Exception('Cant Get email links.')
        except:
            raise Exception('Cant Get email links.')
