def debug(func):
    def wrapper(*args):
        print('Имя функции:', func.__name__, '\nАргументы функции:', *args)
        print(func)
        return func(*args)

    return wrapper


@debug
def mult(dig_1, dig_2, weather):
    return dig_1 * dig_2, weather


print(mult(2, 3, 'sunny'))
