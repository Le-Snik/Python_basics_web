import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, list1, list2, list3, delete=False):
    """
    возвращает n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):

    :param n: количество выдаваемых шуток
    :param list1:  три списка со знкачениями
    :param list2:
    :param list3:
    :param delete: запрещать ли повтор слов. Если TRUE ? то запрещать
    :return:
    """
    list_jokes = []
    if (n > len(list1) or n > len(list2) or n > len(list3)) and delete:
        return None
    for i in range(n):
        rand_ind1 = random.randint(0, len(list1) - 1)
        rand_ind2 = random.randint(0, len(list2) - 1)
        rand_ind3 = random.randint(0, len(list2) - 1)
        list_jokes.append(f"{list1[rand_ind1]} {list2[rand_ind2]} {list3[rand_ind3]}")
        if delete:
            list1.pop(rand_ind1)
            list2.pop(rand_ind2)
            list3.pop(rand_ind3)

    return list_jokes


jokes = get_jokes(5, nouns, adverbs, adjectives, True)
print(jokes)
