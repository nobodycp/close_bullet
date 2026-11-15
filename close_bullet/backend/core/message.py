import random
import time

from close_bullet.backend.style import Box, Colors, Write


class Message:
    @staticmethod
    def welcome(name):
        _hello = Box.Lines(f'Welcome  {name}\nCoded By : https://t.me/Mnaek_Kabsha', pepite=' 💀 ')
        color = Colors.all_colors[random.randrange(0, len(Colors.all_colors))]
        Write.Print(_hello, color, interval=0.005)

    @staticmethod
    def color(message, timeout=10, interval=0.1):
        color = Colors.all_colors[random.randrange(0, len(Colors.all_colors))]
        Write.Print(message, color, interval=interval)
        time.sleep(int(timeout))