# Домашнее задание

import json

decidion = int(input('Введите 1, чтобы начать '))
counter = 1
products_list = {'Номер': {'Название': 'Покупка',
                           'Стоимость': 'Стоимость в рублях'}}
parameters = ['Название', 'Стоимость']

while decidion != 'стоп':
    name_of_product = input('Введите название покупки ')
    price_of_product = float(input('Введите цену покупки '))
    input_data = [name_of_product, price_of_product]
    product_information = dict(zip(parameters, input_data))
    products_list[counter] = product_information
    counter += 1
    decidion = input('Для добавления покупки введите 1, для выхода "стоп" ')

with open('products.json', 'w', encoding='UTF-8') as file:
    json.dump(products_list, file, ensure_ascii=False)

with open('products.json', encoding='UTF-8') as f:
    data = json.load(f)
    result_price = 0
    for item in products_list.items():
        data = item[1]
        for j in data.items():
            if j[1] != 'Покупка' and j[1] != 'Стоимость в рублях' and type(j[1]) != float:
                print(j[1], end=' - ')
            elif type(j[1]) == float:
                result_price += float(j[1])
                print(j[1])
    print('Итоговая сумма за день: ', result_price)
    