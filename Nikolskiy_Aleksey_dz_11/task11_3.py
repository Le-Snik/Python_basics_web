class NoDigit(Exception):
    pass


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
                raise NoDigit
        list_num.append(i_num)
    except NoDigit:
        continue
print(list_num)
