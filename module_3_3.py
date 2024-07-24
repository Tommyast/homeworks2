def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # без аргументов
print_params(16)
print_params(78, 'smth')
print_params('newstr', 9.2, False)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['somesting', 5, False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)
values_list_2 = [3, 'string']
print_params(*values_list_2, 42)
