# Assignment 2
class Calculator:

    def __init__(self):
        self.input_of_digits()

    def input_of_digits(self):
        try:
            self.var_1 = int(input('Введите первое число '))
            self.var_2 = int(input('Введите второе число '))
        except ValueError:
            print('Это не число, попробуйте еще раз)')
            self.input_of_digits()

    def sum_(self):
        sum_result = self.var_1 + self.var_2
        return sum_result

    def subtraction(self):
        subtraction_result = self.var_1 - self.var_2
        return subtraction_result

    def multiplication(self):
        multiplication_result = self.var_1 * self.var_2
        return multiplication_result

    def division(self):
        try:
            division_result = self.var_1 / self.var_2
            return division_result
        except ZeroDivisionError:
            print('Деление на ноль невозможно!')


choice_ = input('Начинаем работу))')
while choice_ != '0':
    calculator = Calculator()
    sign = input('Введите знак: +, -, *, / ')
    if sign == '+':
        print(calculator.sum_())
    elif sign == '-':
        print(calculator.subtraction())
    elif sign == '*':
        print(calculator.multiplication())
    elif sign == '/':
        print(calculator.division())
    else:
        print('Такого знака нет, попробуйте еще раз)')
    choice_ = input('Enter - продолжить, '
                    '0 - завершить ')


# Homework
class Data:

    def input_(self):
        self.input_data = input('Введите  число или строку ')

    def finding_length(self):
        self.length = len(self.input_data)


data_ = Data()
data_.input_()
data_.finding_length()

vowels = 'а е ё и о у ы э ю я a e i o u y'
consonants = 'б в г д ж з й к л м н п р с т ф х ц ч ш щ b c d f g h j k l m n p q r s t v w x z'

if data_.input_data.isdigit():
    sum_of_even = 0
    for i in data_.input_data:
        if int(i) % 2 == 0:
            sum_of_even += int(i)
    print(sum_of_even * data_.length)
else:
    vowels_count = 0
    consonants_count = 0
    for i in data_.input_data:
        if i.lower() in vowels:
            vowels_count += 1
        elif i.lower() in consonants:
            consonants_count += 1
    if vowels_count * consonants_count <= data_.length:
        for i in data_.input_data:
            if i.lower() in vowels:
                print(i)
    else:
        for i in data_.input_data:
            if i.lower() in consonants:
                print(i)
