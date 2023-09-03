from . import userdata
from .options import Randoms as Random
import requests


class Requests:
    @staticmethod
    def proxy_session(Proxy=False):
        s = requests.Session()
        if Proxy:
            s.proxies = {
                'http': f'{userdata["Proxy.type"]}://{Random.proxy()}',
                'https': f'{userdata["Proxy.type"]}://{Random.proxy()}',
            }
            return s
        else:
            if userdata['Proxy.active']:
                # print(Random.proxy())
                s.proxies = {
                    'http':f'{userdata["Proxy.type"]}://{Random.proxy()}',
                    'https':f'{userdata["Proxy.type"]}://{Random.proxy()}',
                }
                return s
            else:
                return s

