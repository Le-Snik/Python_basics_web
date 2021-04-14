import sys
import datetime


class NewDate:
    def __init__(self, str_date):
        NewDate.str_date = str(str_date)

    @classmethod
    def get_date(cls):

        try:
            lst = cls.str_date.split('-')

            cls.day = int(lst[0])
            cls.month = int(lst[1])
            cls.year = int(lst[2])
            cls._valid = True
        except IndexError:
            print("неправильный формат даты")
            cls._valid = False
        except (AttributeError, ValueError):
            print("Дата должна состоять только из цифр")
            cls._valid = False

    @staticmethod
    def valid_date():
        if NewDate._valid:
            try:
                NewDate.as_date = datetime.date(NewDate.year, NewDate.month, NewDate.day)
            except ValueError as err:
                NewDate._valid = False
                print(err)


my_date = NewDate(str(sys.argv[1]))

NewDate.get_date()
NewDate.valid_date()
if NewDate._valid:
    print(f"{NewDate.as_date.day} {NewDate.as_date.month} {NewDate.as_date.year}")
