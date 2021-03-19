names_list = ["Иван", "Мария", "Петр", "Илья", "Игорь","Олег","Татьяна"]

names_dict = {i[0]: [] for i in names_list}
for idx in names_list :
    names_dict[idx[0]].append(idx)
print()


