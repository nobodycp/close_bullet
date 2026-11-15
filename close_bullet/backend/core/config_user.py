import configparser
import subprocess

from close_bullet.backend.constants import sys

if "macos" not in sys:
    import win32console
    import win32gui


class User:
    def __init__(self):
        self.config_file = self.open_file()
        self.data = {}
        self.format_data()
        if self.data["Root.screen_resize"] == 1:
            self.terminal(int(self.data["Root.x"]), int(self.data["Root.y"]))
        self.data["hwid"] = self.hwid()

    @classmethod
    def hwid(cls):
        if "macos" in sys:
            hwid = subprocess.run(
                "system_profiler SPHardwareDataType | grep 'Hardware UUID' | awk '{print $3}'",
                stdout=subprocess.PIPE,
                shell=True,
                check=True,
            ).stdout.decode().strip()
            return hwid
        return str(subprocess.check_output("wmic csproduct get uuid")).split("\\r\\n")[1].strip("\\r").strip()

    @classmethod
    def terminal(cls, x=700, y=300):
        if "macos" in sys:
            return
        title = str(win32console.GetConsoleTitle())
        appname = title.split("\\")[-1]
        block_dev = ["python.exe", "py.exe"]
        if appname not in block_dev and title.endswith(".exe"):
            win32console.SetConsoleTitle(f"{appname.strip()}")
            hwnd = win32gui.GetForegroundWindow()
            win32gui.SetWindowPos(hwnd, 0, x, y, 700, 300, 0)

    @staticmethod
    def open_file():
        try:
            with open("config.ini", "r"):
                pass
            file_cfg = configparser.ConfigParser()
            file_cfg.read("config.ini")
            return file_cfg
        except Exception:
            raise Exception("Cant open config.ini file.")

    def format_data(self):
        try:
            for section in self.config_file.sections():
                numbers = ["threads"]
                true = ["true", "1", "y", "yes", "True"]
                false = ["false", "0", "n", "no", "False"]
                for key, value in self.config_file[f"{section}"].items():
                    if value.lower() in true:
                        self.data[f"{section}.{key}"] = 1
                    elif value.lower() in false:
                        self.data[f"{section}.{key}"] = 0
                    elif key in numbers:
                        self.data[f"{section}.{key}"] = int(value)
                    else:
                        self.data[f"{section}.{key}"] = value
        except Exception:
            raise Exception("Cant format user data from confing.ini file.")