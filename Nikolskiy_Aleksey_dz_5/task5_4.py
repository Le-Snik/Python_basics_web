src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Через comprehension будет быстрее всего по скорости
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]


def get_num(lst):
    """ генератор. черерз него оптимизация по памяти

    :param lst: целевой массив
    :return:
    """
    res = (lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1])
    return res


print(result)
rest = list(get_num(src))
print(rest)


