class NewDate:
    def __init__(self, str_date):
        NewDate.str_date = str(str_date)

    @classmethod
    def get_date(cls):
        lst = cls.str_date.split('-')
        try:
            cls.day = int(lst[0])
            cls.month = int(lst[1])
            cls.year = int(lst[2])
        except IndexError:
            print("неправильный формат даты")

    @staticmethod
    def valid_date():
        if not (1 < NewDate.day < 31) or not (1 < NewDate.month < 31):
            print("invalid date")


my_date = NewDate("12-68-1992")

NewDate.get_date()
NewDate.valid_date()

print(f"{NewDate.day} {NewDate.month} {NewDate.year}")
