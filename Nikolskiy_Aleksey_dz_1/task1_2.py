# Создание массива из кубов
cubes = [i ** 3 for i in range(1, 1001, 2)]
###################
devisor = 7
summand = 17

summ_num = 0
for number in cubes:
    num_buff = number
    summ_dig = 0
    ######### подсчет суммы символов
    while num_buff >= 10:
        summ_dig = summ_dig + (num_buff % 10)
        num_buff = num_buff // 10
    summ_dig = summ_dig + num_buff
    ###########

    if summ_dig % devisor == 0:
        summ_num = summ_num + number
print(summ_num)
####################


# +17 к каждому
for i in range(len(cubes)):
    cubes[i] += summand

summ_num = 0
for number in cubes:
    num_buff = number
    summ_dig = 0
    ######### подсчет суммы символов
    while num_buff >= 10:
        summ_dig = summ_dig + (num_buff % 10)
        num_buff = num_buff // 10
    summ_dig = summ_dig + num_buff
    ###########

    if summ_dig % devisor == 0:
        summ_num = summ_num + number

print(summ_num)
