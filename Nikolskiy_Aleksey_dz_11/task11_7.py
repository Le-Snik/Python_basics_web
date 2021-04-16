import re


class ComplexNumber:
    def __init__(self, numb=None, real=0, imagin=0):
        if not numb is None:
            complex_pattern = re.compile(r'(?P<real>[0-9]+)\+(?P<imagin>[0-9]+)j')

            complex_parced = complex_pattern.search(numb)
            if complex_parced is None:
                raise ValueError("Неправильно введено комплексное число")

            self.real = int(complex_parced.group('real'))
            self.imagin = int(complex_parced.group('imagin'))
        else:
            self.real = real
            self.imagin = imagin

    def __str__(self):
        if self.imagin > 0:
            return f'{self.real}+{self.imagin}j'
        elif self.imagin < 0:
            return f'{self.real}{self.imagin}j'
        else:
            return f'{self.real}'

    def __add__(self, other):
        return ComplexNumber(real=self.real + other.real, imagin=self.imagin + other.imagin)

    def __sub__(self, other):
        return ComplexNumber(real=self.real - other.real, imagin=self.imagin - other.imagin)

    def __mul__(self, other):
        return ComplexNumber(real=(self.real * other.real - self.imagin * other.imagin),
                             imagin=(self.imagin * other.real + self.real * other.imagin))


a = ComplexNumber('1+15j')
b = ComplexNumber(real=5, imagin=20)
c = ComplexNumber(real=5)

print(a)
print(b)
print(c)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
