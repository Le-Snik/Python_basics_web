rus = [i.lower() for i in
       ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']]
eng = [i.lower() for i in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']]

ru_eng_tup = zip(rus, eng)


def registry(example, total):
    if example.isupper():
        total = total.upper()
    elif example.istitle():
        total = total.title()
    else:
        total = total.lower()
    return total


def num_translate(tup, word):
    word_buff = word.lower()
    result = ''
    for idx in tup:
        if idx[0] == word_buff:
            result = idx[1]
            result = registry(word, result)
            return result
        if idx[1] == word_buff:
            result = idx[1]
            result = registry(word, result)
            return result

    return "None"


str_For_translate = input("Введите число для перевода ")

print(num_translate(ru_eng_tup, str_For_translate))
