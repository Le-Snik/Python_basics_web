def summ_of_digits(number):
    summ_dig = 0
    while number > 10:
        summ_dig = summ_dig + number % 10
        number = number // 10
    summ_dig = summ_dig + number
    return summ_dig


def summ_of_numbers(mas, devisor):
    summ_num = 0
    for number in mas:
        if summ_of_digits(number) % devisor == 0:
            print(number)
            summ_num = summ_num + number
    print(summ_num)
    return summ_num


def add_num(mas, num):
    for ind in range(len(mas)):
        mas[ind] = mas[ind] + num
    return mas


cubes = [i ** 3 for i in range(1, 1001, 2)]
print(cubes)

summ_of_numbers(cubes, 7)

cubes = add_num(cubes, 17)

summ_of_numbers(cubes, 7)
# 17063185007
