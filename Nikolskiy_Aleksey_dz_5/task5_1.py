def gen_lst(n):
    my_list = [x for x in range(1, n + 1, 2)]
    return my_list


def gen_lst_not_yield(n):
    my_list = (x for x in range(1, n + 1, 2))
    return my_list


def gen_lst_yield(n):
    for x in range(1, n + 1, 2):
        yield x


num = 19
nums = gen_lst_not_yield(num)
print(type(nums))
for ind in nums:
    print(ind)

nums = gen_lst_yield(num)
print(type(nums))
for ind in nums:
    print(ind)

nums = gen_lst(num)
print(type(nums))
for ind in nums:
    print(ind)
