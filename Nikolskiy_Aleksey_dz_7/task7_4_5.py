import os
import sys
import json

my_dict = {0: [0, []]}
my_dict.update({10 ** i: [0, []] for i in range(1, 9)})
pred = 0
num_files = 0
total_files = 0

directory = str(sys.argv[1])
fold_name = (os.path.split(directory)[1])
for root, dirs, files in os.walk(directory):
    for file in files:
        num_files += 1
        for i in my_dict:
            file_size = os.stat(os.path.join(root, file)).st_size
            if (i <= file_size < i * 10) or (file_size == 0 and i == 0):
                my_dict[i][0] += 1
                if file.split('.')[-1] not in my_dict[i][1]:
                    if len(file.split('.')) > 1:
                        my_dict[i][1].append(file.split('.')[-1])
                    elif None not in my_dict[i][1]:
                        my_dict[i][1].append(None)

                total_files += 1

for i in my_dict:
    my_dict[i] = tuple(my_dict[i])

with open(fold_name + '_summary.json', 'w+', encoding='utf-8') as users_json:
    json.dump(my_dict, users_json)
print(my_dict)
print(num_files)
print(total_files)
