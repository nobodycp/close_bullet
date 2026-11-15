import requests

from close_bullet.backend.constants import ROOT_KEY


class Server:
    def __init__(self, _user_data):
        self._user_data = _user_data
        self.hwid = _user_data["hwid"]
        self.server_data = {}
        self.Connect()
        self.format_data()

    def _offline_server_profile(self):
        return {
            "id": 1,
            "full_name": "NoBody",
            "email": "nobody@mnaek-kabsha.gaza",
            "hwID": f"{self.hwid}",
            "max_threads": "500",
            "max_session": "0",
            "panel_username": "0",
            "panel_password": "0",
            "panel_server_ip": "0",
            "number_of_random_to_check": "5",
            "user_group": "0",
            "is_active": True,
            "created_at": "2022-11-13T01:56:36.741185Z",
            "updated_at": "2023-08-10T11:01:08.398564Z",
        }

    def Connect(self):
        if self._user_data.get("Local.offline_mode") == 1:
            self.server_data = self._offline_server_profile()
            return

        payloads = {"key": f"{ROOT_KEY}", "hwID": f"{self.hwid}"}
        try:
            req = requests.post(
                "http://172.86.112.205:8000/api/v1/clients/detail/",
                json=payloads,
            )
            if self.hwid in req.text:
                self.server_data = req.json()
            else:
                self.server_data = {
                    "id": 1,
                    "full_name": "NoBody",
                    "email": "nobody@mnaek-kabsha.gaza",
                    "hwID": "0000000-0000-0000-0000-00000",
                    "max_threads": "1",
                    "max_session": "0",
                    "panel_username": "0",
                    "panel_password": "0",
                    "panel_server_ip": "0",
                    "number_of_random_to_check": "5",
                    "user_group": "0",
                    "is_active": False,
                    "created_at": "2022-11-13T01:56:36.741185Z",
                    "updated_at": "2023-08-10T11:01:08.398564Z",
                }
        except Exception:
            raise Exception("Server Error Connection ..")

    def format_data(self):
        try:
            data = self.server_data
            data.pop("id")
            data.pop("email")
            data.pop("max_session")
            data.pop("created_at")
            data.pop("updated_at")
            for key, value in data.items():
                if key in ("number_of_random_to_check", "max_threads", "user_group"):
                    data[key] = int(value)
        except Exception:
            raise Exception("cant format Root Data ..")