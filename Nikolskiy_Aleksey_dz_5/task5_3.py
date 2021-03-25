tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Егор'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


def get_zip(lst1, lst2):
    for i in range(len(lst1)):
        if i in range(len(lst2)):
            yield lst1[i], lst2[i]
        else:
            yield lst1[i], None


zips = get_zip(tutors, klasses)
print(type(zips))
for ind in zips:
    print(ind)

