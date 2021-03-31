from task6_1 import ip_list


def get_spamer(list_of_ips):
    spamer_ip = ''
    spamer_responses = 0
    set_ips = set(list_of_ips)

    for ip in set_ips:
        ip_count = list_of_ips.count(ip)
        if ip_count > spamer_responses:
            spamer_responses = ip_count
            spamer_ip = ip

    return [spamer_ip, spamer_responses]


spamer = get_spamer(ip_list)

print(f" ip of spamer {spamer[0]}, number of responses = {spamer[1]}")
