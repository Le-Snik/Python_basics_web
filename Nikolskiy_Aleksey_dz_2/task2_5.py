def print_str(list):
    string = ''
    for i in list:
        kop = round(i % 1, 2)
        rub = int(i - kop)
        kop = int(kop * 100)
        if kop < 10:
            kop = '0' + str(kop)
        string = string + f" {rub}руб {kop}коп."
    print(string)


my_goods = [57.8, 46.51, 97, 10.4, 22, 0.2, 56, 99.99]

print_str(my_goods)
my_goods.sort()
print_str(my_goods)
my_goods.reverse()
print_str(my_goods[:5])
