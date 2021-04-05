import re
import sys

email = str(sys.argv[1])
ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
email_pattern = r'(?P<username>[-+0-9a-zA-Z]+)@(?P<domain>[-+0-9a-zA-Z]+\.\w+)'


def email_parse(string, my_pattern):
    email_res = re.search(my_pattern, string)
    if email_res is None:
        raise ValueError(f"Wrong email: {string}")
    my_dict = email_res.groupdict()
    return my_dict


ans_dict = email_parse(email, email_pattern)
print(ans_dict)
