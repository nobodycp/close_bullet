#import cfscrape
import cloudscraper
import requests
from . import Randoms
from .. import userdata


class Requests:
    @staticmethod
    def proxy_session(Proxy=False):
        s = requests.session()
        if Proxy:
            s.proxies = {
                'http': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                'https': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
            }
            return s
        else:
            if userdata['Proxy.active']:
                # print(Random.proxy())
                s.proxies = {
                    'http': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                    'https': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                }
                return s
            else:
                return s

    @staticmethod
    def cloudscraper(Proxy=False):
        s = cloudscraper.create_scraper()
        if Proxy:
            s.proxies = {
                'http': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                'https': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
            }
            return s
        else:
            if userdata['Proxy.active']:
                # print(Random.proxy())
                s.proxies = {
                    'http': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                    'https': f'{userdata["Proxy.type"]}://{Randoms.proxy()}',
                }
                return s
            else:
                return s

#