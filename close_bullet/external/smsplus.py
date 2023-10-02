import requests


class SmsPlus:
    def __init__(self, ip, user, password):
        self.ip: str = ip
        self.user: str = user
        self.password: str = password
        self.ua: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
        self.s = requests.session()
        self.login()

    def login(self):
        headers = {
            'Host': f'{self.ip}',
            'User-Agent': f'{self.ua}',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': f'http://{self.ip}',
            'DNT': '1',
            'Referer': f'http://{self.ip}/',
        }
        payloads = {
            'action': 'save',
            'sub': 'login',
            'username': f'{self.user}',
            'password': f'{self.password}',
        }
        try:
            req = self.s.post('http://167.99.35.211/ajax_form_handler.php', headers=headers, data=payloads)
            if '"status":"ok"' in req.text:
                return 1
            else:
                return 0
        except Exception as e:
            return 0

    def numbers_page_search(self, args: str):
        headers = {
            'Host': f'{self.ip}',
            'User-Agent': f'{self.ua}',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': f'http://{self.ip}',
            'DNT': '1',
            'Referer': f'http://{self.ip}/index.php?page=numbers&sub=numberslist&view=sms',
        }
        payloads = {
            'sub': 'numberslist',
            'subpage': 'numberslist',
            'page': 'numbers',
            'pageview': 'sms',
            'pageviewcnt': '1',
            'pagesearch': f'{args}',
            'pageorder': 'dateAsc',
            'pageno': '1',
            'noclient': 'all',
            'noservice': 'all',
            'nobillgroup': 'all',
            'test_view_type': '1',
            'search_option': '1',
            'action': 'get',
        }
        try:
            req = self.s.post('http://167.99.35.211/ajax_form_handler.php', headers=headers, data=payloads)
            # print(req.text)
            if '{"listcount":1,' in req.text:
                return 1
            else:
                return 0
        except Exception as e:
            return 0
