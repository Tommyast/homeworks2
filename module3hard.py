def calculate_structure_sum(data_structure):
    total_sum = 0

    def process_element(element):
        nonlocal total_sum
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            for item in element:
                process_element(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                process_element(key)
                process_element(value)

    process_element(data_structure)
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
