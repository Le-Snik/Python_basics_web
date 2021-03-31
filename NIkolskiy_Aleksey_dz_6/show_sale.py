import sys

first = 1
second = -1
line_num = 0

if len(sys.argv) > 1:
    first = int(sys.argv[1])
if len(sys.argv) > 2:
    second = int(sys.argv[2])
with open("files//bakery.csv", 'r') as f:
    for i in f:
        line_num += 1
        if line_num >= first:
            print(f"{i[:-1]}")
        if second != -1 and line_num >= second:
            break


