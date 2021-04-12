import time
import colorama
import sys
from colorama import Fore

colorama.init()


def time_out(color, times):
    for _ in reversed(range(0, times)):
        print(f"{color} {_}", end="")
        time.sleep(1)
        print(' '"\r", end="")


class TrafficLight:
    def __init__(self, color='red'):
        self.__color = color
        self.running()

    def running(self):
        if self.__color == 'red':
            time_out(Fore.RED + self.__color, 7)
            self.__color = 'yellow'

        if self.__color == 'yellow':
            time_out(Fore.YELLOW + self.__color, 2)
            self.__color = 'green'

        if self.__color == 'green':
            time_out(Fore.CYAN + self.__color, 10)
            self.__color = 'red'


light1 = TrafficLight()

loops = int(sys.argv[1])
for i in range(0, loops):
    light1.running()
