def find_password(n):
    result = ""
    used_numbers = set()  # Множество для отслеживания использованных чисел

    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) % n == 0 and i not in used_numbers and j not in used_numbers:
                result += f"{i}{j}"
                used_numbers.add(i)
                used_numbers.add(j)
    return result

# Пример использования функции
n = int(input("Введите число от 3 до 20: "))
print(find_password(n))
