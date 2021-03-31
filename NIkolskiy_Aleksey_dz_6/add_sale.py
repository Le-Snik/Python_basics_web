import sys

data = sys.argv[1]+'\n'

with open("files//bakery.csv", 'a', encoding='utf-8') as f:
    f.write(data)

