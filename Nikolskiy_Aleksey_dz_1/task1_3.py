string_proc = ['процент', 'процента ', 'процентов ']
output = ''
percents = 100  # Количество процентов для вывода

for i in range(1, percents + 1):
    if i not in range(11, 15):  # исключение в склонении для 11-14
        if i % 10 == 1:
            output = string_proc[0]
        elif i % 10 in range(2, 5):
            output = string_proc[1]
        else:
            output = string_proc[2]
    else:
        output = string_proc[2]
    print(i, output)
