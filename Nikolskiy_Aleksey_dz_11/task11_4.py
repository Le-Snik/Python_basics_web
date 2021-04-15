from abc import ABC, abstractmethod

import datetime


def add_to_db(db, obj):
    """
    Добавляет объект в базу данных товара , которая является словарем вида
    ключи - id товара , значение ключа - объект товара
    :param db: - база данных, в которую нужно занести объект
    :param obj: сам объект
    :return:
    """
    db[obj.id] = obj


office_equip_database = {}


class Warehouse:
    """
    Класс Склад
    location - фдрес
    size - количество свободного места
    """

    def __init__(self, location, size):
        self.location = location
        self.free_size = size


class OfficeEquip(ABC):
    """
    абстрактный класс офисного оборудования

    при создании объекта автоматически добавляется в БД
    """

    @abstractmethod
    def __init__(self, manufacturer, model, price, size, color, database=office_equip_database):
        self.manufacturer = manufacturer
        self.model = model
        self.price = price
        self.color = color
        self.size = size

        add_to_db(database, self)


class Printers(OfficeEquip):
    id_equip = 15000  # Идентификатор объекта для принтеров

    def __init__(self, manufacturer, model, price, color='white', size=1, print_type='laser', paper_format='A4',
                 print_speed='15', is_colored=True):
        self.is_colored = is_colored
        self.print_type = print_type
        self.paper_format = paper_format
        self.print_speed = print_speed
        self.id = Printers.id_equip
        super().__init__(manufacturer, model, price, size, color)
        Printers.id_equip += 1

    def printing(self, document):
        print(f"{self.manufacturer}{self.model} printing {document}")


class Mfu(Printers):
    id_equip = 16000  # идентификатор объекта для МФУ

    def __init____init__(self, manuf, model, price, color='white', size=1, print_type='laser', paper_format='A4',
                         print_speed='15', scan_type='tablet',
                         copy_speed=10,
                         is_copy=True, is_colored=True):

        self.scan_type = scan_type
        self.copy_speed = copy_speed
        self.is_copy = is_copy
        self.id = Mfu.id_equip
        super().__init__(manuf, model, price, color, print_type, paper_format, print_speed, is_colored, size)
        Mfu.id_equip += 1

    def scanning(self, document):
        print(f"{self.manufacturer}{self.model} scanning {document}")

    def copying(self, document):
        if self.is_copy:
            print(f"{self.manufacturer}{self.model} copying {document}")
        else:
            print(f"{self.manufacturer}{self.model} can't copy")


class Shredders(OfficeEquip):
    id_equip = 17000  # Bltynbabrfnjh объекта для шреддеров

    def __init__(self, manuf, model, price, color, secret_lvl, cutter_type):
        self.secret_lvl = secret_lvl
        self.cutter_type = cutter_type
        self.id = Shredders.id_equip
        super().__init__(self, manuf, model, price, color)

        Shredders.id_equip += 1

    def shredding(self, document):
        print(f"{self.manufacturer}{self.model} shredding {document}")


class Invoice:
    """
    Класс Накладная
    Поля - номер накладной
    словарь из ID и количества

    """
    today_invoices = 0

    def __init__(self, number, suplie):
        self.number = number
        try:
            self.suplie = {i[0].id: int(i[1]) for i in suplie if int(i[1]) > 0}
        except ValueError:
            print('Накладная не создана, количество позиций введено неверно')
        print(f'Создана накладная номер {self.number}, со следующими позициями : {self.suplie}')

    @classmethod
    def make_invoice(cls, lst_suplie):
        """
        Метод создающий накладую
        :param lst_suplie:  список кортежей вида <объект>,<количчество>
        :return: возвращает объект класса Invoice
        """
        Invoice.valid_list(lst_suplie)
        now = datetime.datetime.now()
        number = '_'.join(map(str, [now.year, now.month, now.day, cls.today_invoices]))
        cls.today_invoices += 1
        return Invoice(number, lst_suplie)

    @staticmethod
    def valid_list(suplie):
        for i in suplie:
            if int(i[1]) <= 0:
                print(f'{i[1]} - Некорректное значение количества товара для {i[0].manufacturer} {i[0].model}, запись '
                      f'будет удалена из накладной ')
                suplie.remove(i)

    def get_invoice_size(self, db):
        """
        рассчитывает количество места для размещения поставки по данной накладной
        :param db: база данных товара
        :return: сумму параметра size товаров
        """
        total_size = 0
        for id in self.suplie:
            total_size += db[id].size * self.suplie[id]
        return total_size


Hp_M15W = Printers(manufacturer='HP', model='laserJet M15W', price=9000)
Hp_8013 = Printers(manufacturer='HP', model='OfficeJet Pro 8013', price=1200)

lst_suplies = [(Hp_M15W, 10), (Hp_8013, '5')]
new_invoice = Invoice.make_invoice(lst_suplies)