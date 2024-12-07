def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total, incorrect_count = personal_sum(numbers)
        count = len(numbers) - incorrect_count
        return total / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Вызовы функции с разными вариантами данных
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Корректная коллекция чисел
