class NoDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


list_num = []
i_num = ''
while i_num != 'exit':
    i_num = (input("Ввести число для добавления в список, для выхода введите exit: "))
    try:
        try:
            i_num = int(i_num)
        except ValueError:
            try:
                i_num = float(i_num)
            except ValueError:
                raise NoDigit("Вы ввели не число")
        list_num.append(i_num)
        print("Все верно, число добавлено")
    except NoDigit as err:
        print(err)

        continue
print(*list_num)
