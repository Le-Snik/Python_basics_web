import sys
with open("files//users.csv", 'r', encoding='utf-8') as users_file:
    with open("files//hobby.csv", 'r', encoding='utf-8') as hobby_file:
        users_list = [i[:-1] for i in users_file]
        hobbys_list = [j[:-1].split(',') for j in hobby_file]
        if len(users_list) < len(hobbys_list):
            sys.exit(1)
        elif len(users_list) > len(hobbys_list):
            for i in range(len(users_list) - len(hobbys_list)):
                hobbys_list.append('None')

        users_dict = {i: j for i, j in zip(users_list, hobbys_list)}
print(users_dict)
