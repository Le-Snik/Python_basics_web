
def summ_of_digits(nmb):
    summ_dig = 0
    while nmb >= 10:
        summ_dig = summ_dig + (nmb % 10)
        nmb = nmb // 10
    summ_dig = summ_dig + nmb
    return summ_dig

# Создание массива из кубов
cubes = [i ** 3 for i in range(1, 1001, 2)]
print(len(cubes))
###################


# Подсчет суммы
devisor = 7
summ_num = 0
for number in cubes:
    if summ_of_digits(number) % devisor == 0:
        summ_num = summ_num + number
print(summ_num)
####################

summ_num = 0

for number in cubes:
    if summ_of_digits(number + 17) % devisor == 0:

        summ_num = summ_num + number
print(summ_num)

# 17063185007
