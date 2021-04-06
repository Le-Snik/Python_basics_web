from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        list_ans = [f'{i} : {type(i)},' for i in args]
        list_kans = [f'{i} : {type(i)},' for i in kwargs]

        if len(list_ans) > 0 and len(list_kans) == 0:  # удаляем лишнюю запятую в конце для красоты
            list_ans[-1] = list_ans[-1][:-1]
        elif len(list_kans) > 0:
            list_kans[-1] = list_kans[-1][:-1]

        print(*list_ans, *list_kans)
        dec_func = func(*args, **kwargs)
        print(f'{func.__name__}({dec_func} : {type(dec_func)})')
        return dec_func

    return wrapper


@type_logger
def calc_cube(x, y, z, lst, **arg2):
    return x ** 3


@type_logger
def calc_cube2():
    return 10 ** 3


calc_cube(2, 4, 6, [1, 2, 3], arg1='123', arg2='12243')
calc_cube2()
