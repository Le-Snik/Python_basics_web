from abc import ABCMeta, abstractmethod


class Clothes:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        self._modifier = 1 / 6.5
        self.size = size
        self._multi = self.size
        super().__init__(name)

    def get_cons(self):
        self.cons = round(self._multi * self._modifier + 0.5, 2)
        return self.cons


class Suit(Clothes):

    def __init__(self, name, height):
        self._modifier = 2
        self.height = height
        self._multi = self.height
        super().__init__(name)

    @property
    def get_cons(self):
        self.cons = round(self._multi * self._modifier + 0.5, 2)
        return self.cons


suit = Suit("best_suit", 5)
print(suit.get_cons)

coat = Coat("best_coat", 6)
coat.get_cons()
print(coat.cons)

