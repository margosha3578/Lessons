def division():
    try:
        input_1 = int(input('Введите число 1 '))
        input_2 = int(input('Введите число 2 '))
        result = input_1 / input_2
        print(result)
    except ValueError:
        print('Введены не числа!')
    except ZeroDivisionError:
        print('Деление на ноль невозможно! Повторно введите числа!')
        division()


division()
print('Программа завершена')
