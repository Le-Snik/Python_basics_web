src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
src_res = []
unique_src = set()

# получаем уникальное множество
for i in src:
    if i in unique_src:
        unique_src.remove(i)
    else:
        unique_src.add(i)
print(unique_src)

# Если элемент есть в уникальном множесте, т опереписываем его  в новый список, для сохранения порядкового номера
for i in src:
    if i in unique_src:
        src_res.append(i)

print(src_res)