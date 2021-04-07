import requests
import re

response = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

with open("logs.txt", 'w', encoding='utf-8') as file:
    file.write(str(response.text))

ip_pattern = \
    re.compile(
        r'([\da-f]{1,4}[.:][\da-f]{1,4}[.:][\da-f]{1,4}[.:][\da-f]{1,4})'  # (любая цифра или буква от а до f точка или двоеточие )х4
        r'[^\[]+\[([^\]]+)\]\W+([a-zA-Z]+)([^"]+)\D+(\d+)(\d+)')    # любые символы до [, сама [ , (любые символы до) ] , сама ],
                                                                    # НЕ буквы (буквы и цифры) (любые символы
                                                                    # кроме " )  не цифры (любое количество цифр)(любое количество цифр)

with open("logs.txt", 'r', encoding='utf-8') as file:
    for line in file:
        res = ip_pattern.search(line)
        print(res.groups())
