def add_everything_up(a, b):
    if type(a) != type(b):
        return str(a) + str(b)

    if isinstance(a, str) and isinstance(b, str):
        return a + b

    try:
        a_number = float(a)
    except ValueError as exc:
        print(f'Нельзя конвертировать {a} в число. Ошибка {exc}')


    try:
        b_number = float(b)
    except ValueError as exc:
        print (f'Нельзя конвертировать {b} в число. Ошибка {exc}')

    return a_number + b_number

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))





















# # try:
# #     # код с возможной ошибкой
# # except:
# #     # блок кода в случае возникновения ошибки
#
# try:
#     i = 0
#     print(10 / i)
#     print('сделано')
# except ZeroDivisionError:  # указываем имя класса ошибки
#     print('нельзя делить на ноль')
#
# # в блоке except лучше сразу указывать название класса ошибки
# # Если ошибок несколько их можно перечислять в блоке except (ZeroDivisionError, NameError)
# # или можно создавать несколько блоков except для каждого класса ошибки
#
# try:
#     truba = a + b
#     trube = 10 / 0
# except ZeroDivisionError:
#     print('Нельзя делить на ноль')
# except NameError:
#     print('Нет такой переменной')
#
# # Название ошибки можно записывать в переменную
#
# try:
#     a = 10 / 0
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}')
#
# # В комбинации с try и except используется также else и finally
# # в блоке else пишется код, который будет выполняться, если в коде из блока try не оказалось ошибки.
# # Код из блока finally будет выполняться в любом случае.
#
# print('Сегодня учимся работать с исключениями')
# i = int(input('Введите число: '))
#
# try:
#     result = 10 * (1 / i)
# except ZeroDivisionError as exc:
#     print('Нельзя делить на ноль!', exc)
# else:
#     print('Ура, мы не делим на ноль')
# finally:
#     print('Файнали урок закончен')
