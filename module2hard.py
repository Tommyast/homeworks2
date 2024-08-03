def find_password(n):
    pairs = []

    # Перебираем все возможные пары чисел от 1 до 20
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if (i + j) % n == 0:
                pairs.append((i, j))

    # Формируем строку пар
    result = ''.join([f"{i}{j}" for i, j in pairs])
    return result


# Пример использования
n = int(input("Введите число от 3 до 20: "))
result = find_password(n)
print(f"Пароль для числа {n}: {result}")
