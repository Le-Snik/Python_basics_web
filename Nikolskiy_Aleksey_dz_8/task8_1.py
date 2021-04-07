import re
import sys

email = str(sys.argv[1])
email_pattern = re.compile(r'(?P<username>[-+0-9a-zA-Z]+)@(?P<domain>[-+0-9a-zA-Z]+\.\w{2,})')


def email_parse(string, my_pattern):
    email_res = my_pattern.search(string)
    if email_res is None:
        raise ValueError(f"Wrong email: {string}")
    my_dict = email_res.groupdict()
    return my_dict


ans_dict = email_parse(email, email_pattern)
print(ans_dict)
