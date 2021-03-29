import requests

response = requests.get(
    'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')

with open("logs.txt", 'w', encoding='utf-8') as file:
    file.write(str(response.text))

with open("logs.txt", 'r', encoding='utf-8') as file:
    tuple_lst = []
    ip_list = []
    for line in file:
        buff_lst = []
        ip = line.split(' ')[0]
        ip_list.append(ip)
        get = (line.split('"')[1].split(" ")[:2])
        buff_lst.append(ip)
        buff_lst.extend(get)
        tuple_lst.append(tuple(buff_lst))

if __name__ == '__main__':
    for tup in tuple_lst:
        print(tup)
