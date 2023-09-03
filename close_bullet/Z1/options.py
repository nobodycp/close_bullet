import base64
import random
import re
import urllib
import uuid
import names
import phonenumbers
from phonenumbers import carrier,timezone
import pycountry
from phone_iso3166.country import phone_country
from urllib.parse import unquote
from . import lists

class Phone:
    """
    Example:
        * phone=Phone('+972567108204')
        * print(phone.number)
    Attributes:
        number
        prefix
        local
        zero_lod
        alpha_2
        name
        carrier
        time_zone
        local
    """
    def __init__(self, number:str):
        self.number = f'+{number.replace("+", "")}'
        self.prefix = phonenumbers.parse(self.number).country_code
        self.local = phonenumbers.parse(self.number).national_number
        self.international = phonenumbers.format_number(phonenumbers.parse(self.number), phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        self.zero_lod = phonenumbers.format_number(phonenumbers.parse(self.number), phonenumbers.PhoneNumberFormat.NATIONAL)
        self.alpha_2 = phone_country(number)
        if self.prefix == 383:
            self.alpha_3 = 'XXK'
            self.name = 'Kosovo'
        else:
            self.alpha_3 = pycountry.countries.get(alpha_2=self.alpha_2).alpha_3
            self.name = pycountry.countries.get(alpha_2=self.alpha_2).name
        self.carrier = carrier.name_for_number(phonenumbers.parse(number, self.alpha_2), "en")
        self.time_zone = timezone.time_zones_for_number(phonenumbers.parse(self.number, self.alpha_2))
class Randoms:
    @staticmethod
    def proxy()->str:
        return str(random.choice(lists.proxy)).strip()
    @staticmethod
    def device_id()->str:
        return str(uuid.uuid4()).strip()
    @staticmethod
    def user_agent()->str:
        return str(random.choice(lists.user_agents)).strip()

    @staticmethod
    def strings(length:int, mode)->str:
        return ''.join(random.choice(mode) for _ in range(int(length)))
    @staticmethod
    def from_list(YourList:list):
        return random.choice(YourList)
class FakeName:
    """
    Example:
        * name = FakeName(sex='male', domain='gmail.com')
        * print(name.full_name)
    Attributes:
        title
        first_name
        last_name
        full_name
        email
    """
    def __init__(self, sex:str=random.choice(('male', 'female')) ,domain:str='gmail.com'):
        if sex.lower() == 'male':
            title = 'Mr'
        else:
            title = 'Ms'
        self.title = title
        self.first_name = names.get_first_name(sex.lower())
        self.last_name = names.get_last_name()
        self.full_name = f'{self.first_name} {self.last_name}'
        self.email = self.full_name.replace(' ', random.choice(['_', '.', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])) + f'@{domain}'

class Options:
    @staticmethod
    def parse_text(text: str, before: str, after: str) -> str:
        return re.search(f'{before}(.*?){after}', text).group(1).strip().rstrip()
    @staticmethod
    def header_parse(headers_: str) -> dir(): # type: ignore
        headers = {}
        for i in headers_.strip().split('\n'):
            i = i.strip()
            try:
                key = i.split(': ')[0]
                value = i.split(': ')[1]
                # print(f'{key} {value}')
                headers[f'{key.lower()}'] = f'{value}'
            except:
                pass
        return headers
    @staticmethod
    def payload_parse(payloads_: str) -> dir(): # type: ignore
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
        return urllib.parse.unquote(text)

Option = Options()
