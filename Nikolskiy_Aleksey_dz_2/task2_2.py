my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', 'а', 'воды', '-10']
signs = ['-', '+']

i = 0
while i != len(my_list):
    if my_list[i].isdigit() or ((my_list[i][0] in signs) and my_list[i][1:].isdigit):  # Если элемент целиком из цифр,
        # или первый символ элемента +- а в остальном он из цифр
        if my_list[i].isdigit() and int(my_list[i]) < 10:  # Добавялем 0 , если не двузначный
            my_list[i] = "0" + my_list[i]
        elif (my_list[i][0] in signs) and my_list[i][1:].isdigit and int(my_list[i][1:]) < 10: #для элементов со знаком
            my_list[i] = my_list[i][0] + "0" + my_list[i][1:]
        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 1
    i += 1


print(' '.join(my_list))

