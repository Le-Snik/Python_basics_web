import sys


def file_work(dir_users, dir_hobby, dir_total):
    with open(dir_users, 'r', encoding='utf-8') as users_file:
        with open(dir_hobby, 'r', encoding='utf-8') as hobby_file:
            users_list = [i[:-1] for i in users_file]
            hobbys_list = [j[:-1] for j in hobby_file]
            if len(users_list) < len(hobbys_list):
                sys.exit(1)
            elif len(users_list) > len(hobbys_list):
                for i in range(len(users_list) - len(hobbys_list)):
                    hobbys_list.append('None')

            users_list = [':'.join([i, ' ' + j]) for i, j in zip(users_list, hobbys_list)]

    with open(dir_total, 'w', encoding='utf-8') as users_hobby:
        for st in users_list:
            users_hobby.write(st + '\n')


if __name__ == '__main__':
    file_work("files//users.csv", "files//hobby.csv", "files//users_hobby.txt")
