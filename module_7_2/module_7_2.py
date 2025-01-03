def custom_write(file_name, strings):
    file = open('module_7_2.txt', 'w', encoding='utf-8')

    strings_position = {}

    for index, string in enumerate(strings):
        position = file.tell()

        file.write(string + '\n')
        strings_position[(index + 1, position)] = string

    file.close()
    return strings_position


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
