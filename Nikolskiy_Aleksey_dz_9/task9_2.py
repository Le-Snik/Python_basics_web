class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, mass_min, thick):
        all_mass = self._length * self._width * mass_min * thick/1000
        return all_mass


mkad = Road(length=5000, width=20)

print(mkad.get_mass(25, 5))
