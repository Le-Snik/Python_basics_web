names_list = ["Иван", "Мария", "Петр", "Илья", "Игорь", "Олег", "Татьяна"]
lastnames_list = ["Иван Таранов", "Мария Иванова", "Петр Романов", "Илья Муромец", "Игорь Григорьев", "Олег Олегов",
                  "Татьяна Белая", "Егор Тирский", "Василий Рыжов", "Иннокентий Танов"]


def sort_dict(dictionar):
    """ Сортирует словарь по ключам. Возвращает новый словарь

    :param dictionar:  словарь для сортировки
    :return:  возвращаемый новый отсортированный по ключам словарь
    """
    new_dict = {}
    list_keys = list(dictionar.keys())
    list_keys.sort()
    for ind in list_keys:
        new_dict[ind] = dictionar[ind]
    return new_dict


def make_dict(lst):
    """ Создает словарь из списка имен ,
    ключами являются первые буквы

    :param lst: - список , по первым буквам каждого элемента которого создается словарь
    :return: созданный словарь
    """
    new_dict = {i[0]: [] for i in lst}
    for name in lst:
        new_dict[name[0]].append(name)
    return (new_dict)


def thesaurus_adv(lst):
    """ возвращает словарь, в котором ключи — первые буквы фамилий, а значения — словари,
    содержащие записи, в которых фамилия начинается с соответствующей буквы

    :param lst: список имен и фамилий, разделенных пробелом
    :return:
    """
    buff_lst = lst.copy()
    lst_of_names = []
    for i in range(len(buff_lst)):
        buff_lst[i] = buff_lst[i].split(" ")

    new_dict = {i[1][0]: [] for i in buff_lst}

    for let in new_dict:  # Идем по всем ключам словаря
        lst_of_names = []
        for name in buff_lst:  # идем по всему списку имен
            if name[1][0] == let:  # Если фамилия начинается с ключа словаря, добавляем в список
                lst_of_names.append(" ".join(name))
        new_dict[let] = make_dict(
            lst_of_names)  # Вызываем предыдущую функцию, что бы создать словарь с выбранным списком
    return new_dict


lastnames_dict = make_dict(lastnames_list)
thes_lastnames_dict = thesaurus_adv(lastnames_list)

sorted_dict = sort_dict(thes_lastnames_dict)
print(thes_lastnames_dict)
print(sorted_dict)
