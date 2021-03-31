import sys
import os

second = -1
line_num = 0

num_edit_line = int(sys.argv[1])
edit_line = sys.argv[2]

with open("files//bakery.csv", 'r+') as f:
    with open("files//bakery_temp.csv", 'w') as f2:
        for line in f:
            line_num += 1
            if line_num == num_edit_line:
                f2.write(edit_line + '\n')
            else:
                f2.write(line)
os.remove("files//bakery.csv")
os.rename("files//bakery_temp.csv", "files//bakery.csv")
