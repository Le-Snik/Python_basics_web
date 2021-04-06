from functools import wraps


def val_checker(condition):
    def logger(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not condition(arg):
                    mes = f'Wrong val :{arg}'
                    raise ValueError(mes)
                dec_func = func(*args, **kwargs)
            return dec_func

        return wrapper

    return logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """
тестовая функция.
:return: возвращает куб числа Х
  """
    return x ** 3


print(calc_cube.__doc__)
print(calc_cube(-5))
