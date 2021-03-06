class Cell:
    def __init__(self, numb):
        self.numb = int(numb)

    def __add__(self, other):
        plus = self.numb + other.numb
        new_cell = Cell(plus)
        return new_cell

    def __sub__(self, other):
        minus = self.numb - other.numb
        if minus > 0:
            new_cell = Cell(minus)
            return new_cell
        else:
            print("Вычитание  невозможно, разнность меньше нуля ")

    def __mul__(self, other):
        mult = self.numb * other.numb
        new_cell = Cell(mult)
        return new_cell

    def __truediv__(self, other):
        dive = self.numb // other.numb
        new_cell = Cell(dive)
        return new_cell

    def __floordiv__(self, other):
        self.__truediv__(self, other)

    def make_order(self, nums):
        str_lst = ['*' * nums for i in range(0, self.numb // nums)]
        str_lst.append('*' * (self.numb % nums)+'\n')
        return "\n".join(str_lst)


my_cell = Cell(50)
print(f"{my_cell.numb}\n{my_cell.make_order(10)}")

my_cell2 = Cell(11)

my_cell3 = my_cell - my_cell2
print(f"{my_cell3.numb}\n{my_cell3.make_order(10)}")
my_cell3 = my_cell + my_cell2
print(f"{my_cell3.numb}\n{my_cell3.make_order(10)}")
my_cell3 = my_cell * my_cell2
print(f"{my_cell3.numb}\n{my_cell3.make_order(10)}")
my_cell3 = my_cell / my_cell2
print(f"{my_cell3.numb}\n{my_cell3.make_order(10)}")
