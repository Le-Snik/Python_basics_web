import os
import sys

my_dict = {0: 0}
my_dict.update({10 ** i: 0 for i in range(1, 8)})
pred = 0
num_files = 0
total_files = 0

directory = str(sys.argv[1])
for root, dirs, files in os.walk(directory):
    for file in files:
        num_files += 1
        for i in my_dict:
            file_size = os.stat(os.path.join(root, file)).st_size
            if file_size == 0 and i == 0:
                my_dict[i] += 1
                total_files += 1
            elif i <= file_size < i * 10:
                my_dict[i] += 1
                total_files += 1

print(my_dict)
print(num_files)
print(total_files)
