import sys


class MyDivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    if int(sys.argv[2]) != 0:
        print(int(sys.argv[1]) / int(sys.argv[2]))
    else:
        raise MyDivisionZero("Деление на ноль")
except MyDivisionZero as err:
    print(err)
