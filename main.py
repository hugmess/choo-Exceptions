result = []
def divider(a, b):
     if a < b:
         raise ValueError ('Число "а" меньше числа "b" ')
     print('Невозможно посчитать результат')
     if b > 100:
         raise IndexError (" индекс является недопустимым")
     print('индекс выходит за границы, будучи слишком большим')
     return a/b

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4};
except IndentationError as error:
    print(f'Пробелы или табуляции расставлены неправильно {error}')
except TypeError as error:
    print(f'Разные типы данных. {error}')
except NameError as error:
    print(f'Переменная не существует, либо была использована недопустимым образом')
except Exception as error:
    print(f'Неопредвиденная ошибка: {type(error)}: {error}')
else:
    print('Всё нормик!')


try:
    for key in data:
         res = divider(key, data[kem])
         result.append(res)

except NameError as error:
    print(f'Переменная не существует, либо была использована недопустимым образом')
except Exception as error:
    print(f'Неопредвиденная ошибка: {type(error)}: {error}')


print(result)
