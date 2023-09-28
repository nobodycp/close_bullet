import re, base64, random, string, urllib, uuid,names,phonenumbers,pycountry
from datetime import datetime, timedelta
from phonenumbers import carrier, timezone
from phone_iso3166.country import phone_country
from urllib.parse import unquote
from .. import lists


class Phone:
    def __init__(self, number: str):
        self.full = f'+{number.replace("+", "")}'
        self.prefix = phonenumbers.parse(self.full).country_code
        self.local = phonenumbers.parse(self.full).national_number
        self.international = phonenumbers.format_number(phonenumbers.parse(self.full),phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        self.zero_lod = phonenumbers.format_number(phonenumbers.parse(self.full),phonenumbers.PhoneNumberFormat.NATIONAL)
        self.alpha_2 = phone_country(number)
        if self.prefix == 383:
            self.alpha_3 = 'XXK'
            self.name = 'Kosovo'
        else:
            self.alpha_3 = pycountry.countries.get(alpha_2=self.alpha_2).alpha_3
            self.name = pycountry.countries.get(alpha_2=self.alpha_2).name
        self.carrier = carrier.name_for_number(phonenumbers.parse(number, self.alpha_2), "en")
        self.time_zone = timezone.time_zones_for_number(phonenumbers.parse(self.full, self.alpha_2))

class Randoms:
    @staticmethod
    def proxy() -> str:
        return str(random.choice(lists.proxys)).strip()

    @staticmethod
    def device_id() -> str:
        return str(uuid.uuid4()).strip()

    @staticmethod
    def user_agent() -> str:
        return str(random.choice(lists.user_agents)).strip()

    @staticmethod
    def strings(length: int, mode) -> str:
        return ''.join(random.choice(mode) for _ in range(int(length)))

    @staticmethod
    def from_list(YourList: list):
        return random.choice(YourList)

class FakeInfo:
    def __init__(self, domain: str = 'gmail.com'):
        sex:str = random.choice(('male', 'female'))
        if sex.lower() == 'male':
            title = 'Mr'
        elif sex.lower() == 'female':
            title = 'Ms'
        self.title:str = title
        self.first:str = names.get_first_name(sex.lower())
        self.last:str = names.get_last_name()
        self.full:str = f'{self.first} {self.last}'
        self.email:str = self.full.replace(' ', random.choice(['_', '.', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) + f'@{domain}'
        self.date_of_birth:str = self.dob()
        self.sex:str = sex
        self.password:str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '@!#$%^') for _ in range(15))

    @staticmethod
    def dob(split_type='-'):
        start_date = datetime(1950, 1, 1)
        end_date = datetime(2005, 12, 31)
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date.strftime(f"%Y{split_type}%m{split_type}%d")

class Options:
    @staticmethod
    def parse_text(text: str, before: str, after: str) -> str:
        return re.search(rf'{before}(.*?){after}', text).group(1).strip().rstrip()

    @staticmethod
    def header_parse(headers_: str, lower:bool=False) -> dict:  # type: ignore
        headers = {}
        for i in headers_.strip().split('\n'):
            try:
                key, value = i.strip().split(': ', maxsplit=2)
                if lower:
                    headers[f'{str(key).lower()}'] = f'{value}'
                else:
                    headers[f'{key}'] = f'{value}'
            except:
                pass
        return headers

    @staticmethod
    def payload_parse(payloads_: str) -> dict:  # type: ignore
        decode = unquote(unquote(payloads_))
        payloads = {}
        try:
            for i in decode.split('&'):
                key = i.split('=')[0].strip()
                value = i.split('=')[1].strip()
                payloads[f'{key}'] = f'{value}'
        except:
            pass
        return payloads

    @staticmethod
    def image_to_base64(image):
        return base64.b64encode(image).decode()

    @staticmethod
    def url_decode(text):
        return urllib.urlencode(text)
    @staticmethod
    def url_encoded(text):
        return urllib.parse.quote_plus(text)