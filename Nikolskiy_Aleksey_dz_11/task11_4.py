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


office_equip_database = {}  # База данных товаров
set_enabled_goods = set()  # множество разрешенных товаров


class Warehouse_db_object:
    """
    объект базы данных склада
    db- база данных товаров, из которой этот объект
    quant - количество на данном складе
    """

    def __init__(self, quant, db):
        self.db = db
        self.quant = quant


class Warehouse:
    """
    Класс Склад
    location - фдрес
    size - количество свободного места
    """

    def __init__(self, location, size):
        self.location = location
        self.free_size = size
        self.list_of_goods = {}

    def get_goods(self, invoice):
        """
        Получение товара.
        :param invoice: Накладная
        """
        inv_size = invoice.get_invoice_size()  # место занимаемое получаемой поставкой
        if self.free_size >= inv_size:
            for i in invoice.suplie:
                if i not in self.list_of_goods:  # если такого товара нет на складе, то добавляем его в список товаров
                    self.list_of_goods[i] = Warehouse_db_object(quant=invoice.suplie[i],
                                                                db=invoice.database)
                else:
                    self.list_of_goods[i].quant += invoice.suplie[i]  # если такой товар уже есть, то просто
                    # увеличиваем количество
            self.free_size -= inv_size  # уменьшаем количество оставшегося свободного места
            print(f'Товар получен по накладной {invoice.number}')
        else:
            print('Невозможно принять товар, недостаточно свободного места')

    def send_goods(self, invoice):
        """
        Выгрузка товара
        :param invoice: накладная
        """
        for i in invoice.suplie:
            if invoice.suplie[i] <= self.list_of_goods[i].quant:
                self.list_of_goods[i].quant -= invoice.suplie[i]
                if self.list_of_goods[i].quant == 0:
                    self.list_of_goods.pop(i)
            else:
                print(f"Невозможно отгрузить товар по накладной {invoice.number} , товар в необходимом количестве "
                      f"отсутсвует на складе. ")

    def show_all_goods(self):
        """
        Показывает все товары на складе
        :return:
        """
        if len(self.list_of_goods) == 0:
            print("Склад пуст")
        else:
            print(f'Всего на складе:')
            for i in self.list_of_goods:
                print(
                    f'{self.list_of_goods[i].db[i].manufacturer} {self.list_of_goods[i].db[i].model}, количество - {self.list_of_goods[i].quant}')

    def get_invoice(self, inv):
        """
        обработка накладной. В зависисмоти от ее типа ( на ввоз или на вывоз) вызывает соответствующий метод
        :param inv: накладная
        :return:
        """
        if inv != None:
            if inv.input:
                self.get_goods(inv)
            else:
                self.send_goods(inv)
        else:
            print("Принята пустая накладная")


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
        set_enabled_goods.add(type(self))
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

    def __init__(self, manuf, model, price, color='white', size=1, print_type='laser', paper_format='A4',
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
    id_equip = 17000  # Идентификатор объекта для шреддеров

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

    """
    today_invoices = 0  # Количество накладных сегодня, нужно для формирования номера накладной

    def __init__(self, number, suplie, database, in_put='input'):
        """
        :param number: номер накладной
        :param suplie: словарь где ключ -  ID , значение - количество товара с этим ID
        :param database: база данных, из которой берутся товары
        :param in_put: True - накладная на ввоз
            Else - накладная на вывоз
        """
        self.number = number
        self.database = database
        if in_put == 'input':
            self.input = True
            st_out = "на ввоз"
        elif in_put == 'output':
            self.input = False
            st_out = 'на вывоз'
        try:
            self.suplie = {i[0].id: int(i[1]) for i in suplie if int(i[1]) > 0}
        except ValueError:
            print('Накладная не создана, количество позиций введено неверно')
        print(f'Создана накладная {st_out} номер {self.number}, со следующими позициями :')
        for i in self.suplie:
            print(f'{self.database[i].manufacturer} {self.database[i].model} , количество {self.suplie[i]}')

    @classmethod
    def make_invoice(cls, lst_suplie, database, in_put='input'):
        """
        Метод создающий накладую
        :param in_put: на ввоз или на вывоз
        :param database: база данных товара, из которой создается поставка
        :param lst_suplie:  список кортежей вида <объект>,<количчество>
        :database - бд товаров в накладной
        :return: возвращает объект класса Invoice
        """
        if Invoice.valid_list(lst_suplie):
            now = datetime.datetime.now()
            number = '_'.join(map(str, [now.year, now.month, now.day, cls.today_invoices]))
            cls.today_invoices += 1
            return Invoice(number, lst_suplie, database, in_put)
        else:
            print('список товаров пуст, накладная не создана')
            return None

    @staticmethod
    def valid_list(suplie):
        """
        проверяет список поставки/
        Если товар не в списке разрешенных товаров, или если количество введено неверно, то адаляет его из списка
        :param suplie:
        :return: false если все в списке удалено
        """
        lst_to_remove = []
        for i in suplie:
            if type(i[0]) not in set_enabled_goods:
                print(f'{i[0]} - некорректный товар, запись будет удалена из накладной ')
                lst_to_remove.append(i)
                continue

            if int(i[1]) <= 0:
                print(
                    f'{i[1]} - Некорректное значение количества товара для {i[0].manufacturer} {i[0].model}, запись '
                    f'будет удалена из накладной ')
                lst_to_remove.append(i)
                continue

        for i in lst_to_remove:
            suplie.remove(i)
        if len(suplie) == 0:
            return False
        else:
            return True

    def get_invoice_size(self):
        """
        рассчитывает количество места для размещения поставки по данной накладной
        :param db: база данных товара
        :return: сумму параметра size товаров
        """
        total_size = 0
        for id in self.suplie:
            total_size += self.database[id].size * self.suplie[id]
        return total_size


Hp_M15W = Printers(manufacturer='HP', model='laserJet M15W', price=9000)
Hp_8013 = Printers(manufacturer='HP', model='OfficeJet Pro 8013', price=12000)

new_warehouse = Warehouse(location='Moscow', size=100)

lst_suplies = [(Hp_M15W, 10), (Hp_8013, 5)]

new_warehouse.get_invoice(Invoice.make_invoice(lst_suplies, office_equip_database))
new_warehouse.get_invoice(Invoice.make_invoice(lst_suplies, office_equip_database))
new_warehouse.get_invoice(Invoice.make_invoice(lst_suplies, office_equip_database))
new_warehouse.get_invoice(Invoice.make_invoice(lst_suplies, office_equip_database))

new_warehouse.show_all_goods()

# new_invoice_out = Invoice.make_invoice(lst_suplies, office_equip_database, in_put='output')
#
# new_warehouse.get_invoice(new_invoice_out)
# new_warehouse.show_all_goods()
