my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(my_list)):
    my_list[i] = my_list[i].title()
    my_list[i] = my_list[i].split(' ')
    print("Привет,", my_list[i][-1])

