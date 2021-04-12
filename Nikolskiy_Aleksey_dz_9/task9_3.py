class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = " ".join([self.name, self.surname])
        return full_name

    def get_total_income (self):
        total_income = self._income["wage"] + self._income["bonus"]
        return total_income


ingener = Position(name="Alex", surname='N', position='programmer', wage=100, bonus=10)


print(vars(ingener))
print(ingener.get_full_name())
print(ingener.get_total_income())
