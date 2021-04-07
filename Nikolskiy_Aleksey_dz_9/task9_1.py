import time


class TrafficLight:
    def __init__(self, color='red'):
        self.__color = color
        #self.running()

    def running(self):
        if self.__color == 'red':
            print(self.__color)
            time.sleep(7)
        if self.__color == 'yellow':
            print(self.__color)
            time.sleep(2)
            self.__color = 'green'
        if self.__color == 'green':
            print(self.__color)
            time.sleep(10)
            self.__color = 'red'


light1 = TrafficLight()
light1.running()

