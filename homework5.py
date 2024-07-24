# immutable_var = 1, 2, True, "String"
# print(immutable_var)
# immutable_var[2] = False

# 1. Кортежи занимают меньше места чем списки и это может быть способом оптимизации кода 2. Кортежи могут упростить
# понимание кода, так как разработчик будет уверен и спокоен, что элементы кортежа не изменятся 3. Возможно,
# изменяемые кортежи могли бы привести к ошибкам в программах


mutable_list = ["PlayStation", "Xbox", "Nintendo", "PC", False, 11]
mutable_list.remove(False)
mutable_list.append(True)
print(mutable_list)
