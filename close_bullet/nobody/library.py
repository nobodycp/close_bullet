#import cfscrape
import cloudscraper
import requests

from . import Randoms
from .http_errors import wrap_session_request
from .. import userdata


class Requests:
    @staticmethod
    def _apply_proxies(s, prefer_proxy: bool):
        # [Proxy] active in config.ini is the master switch (off = no proxy in code).
        # When active=1: use proxy (prefer_proxy=True marks script intent; default path also uses proxy).
        if userdata["Proxy.active"]:
            proxy = Randoms.proxy()
            ptype = userdata["Proxy.type"]
            s.proxies = {
                "http": f"{ptype}://{proxy}",
                "https": f"{ptype}://{proxy}",
            }
        return wrap_session_request(s)

    @staticmethod
    def proxy_session(Proxy=False):
        s = requests.Session()
        return Requests._apply_proxies(s, Proxy)

    @staticmethod
    def cloudscraper(Proxy=False):
        s = cloudscraper.create_scraper()
        return Requests._apply_proxies(s, Proxy)