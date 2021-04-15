from abc import ABC, abstractmethod
import re

import datetime


class OfficeEquip(ABC):
    @abstractmethod
    def __init__(self, manuf, model, price, color, size):
        self.manufacturer = manuf
        self.model = model
        self.price = price
        self.color = color
        self.size = size


class Printers(OfficeEquip):
    def __init__(self, manuf, model, price, color, size, print_type, paper_format, print_speed, is_colored=True):
        super().__init__(self, manuf, model, price, color, size)
        self.is_colored = is_colored
        self.print_type = print_type
        self.paper_format = paper_format
        self.print_speed = print_speed

    def printing(self, document):
        print(f"{self.manufacturer}{self.model} printing {document}")


class Mfu(Printers):
    def __init____init__(self, manuf, model, price, color, size, print_type, paper_format, print_speed, scan_type,
                         copy_speed,
                         is_copy=True, is_colored=True):
        super().__init__(self, manuf, model, price, color, print_type, paper_format, print_speed, is_colored, size)
        self.scan_type = scan_type
        self.copy_speed = copy_speed
        self.is_copy = is_copy

    def scanning(self, document):
        print(f"{self.manufacturer}{self.model} scanning {document}")

    def copying(self, document):
        if self.is_copy:
            print(f"{self.manufacturer}{self.model} copying {document}")
        else:
            print(f"{self.manufacturer}{self.model} can't copy")


class Shredders(OfficeEquip):
    def __init__(self, manuf, model, price, color, secret_lvl, cutter_type):
        super().__init__(self, manuf, model, price, color)
        self.secret_lvl = secret_lvl
        self.cutter_type = cutter_type

    def shredding(self, document):
        print(f"{self.manufacturer}{self.model} shredding {document}")


class Invoice:
    def __init__(self, number, suplie):
        self.number = number
        self.suplie = {i[0]: i[1] for i in suplie}


today_invoices = 0


def make_invoice(lst_suplie, today_invoices):
    now = datetime.datetime.now()
    number = '_'.join(map(str, [now.year, now.month, now.day, today_invoices]))

    return Invoice(number, lst_suplie)


lst_suplies = [('canon', 1), ('Hp', 10)]
new_invoice = make_invoice(lst_suplies, today_invoices)
today_invoices += 1
new_invoice2 = make_invoice(lst_suplies, today_invoices)
today_invoices += 1

print(new_invoice.number)
print(new_invoice2.number)
