def calculate_structure_sum(data):
    def recursive_sum(item):
        number = 0

        if isinstance(item, int):
            number += item
        elif isinstance(item, str):
            number += len(item)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                number += recursive_sum(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                number += recursive_sum(key)
                number += recursive_sum(value)
        elif isinstance(item, bool):
            number += int(item)

        return number

    return recursive_sum(data)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summa = calculate_structure_sum(data_structure)
print("Подсчёт суммы всех чисел и длин всех строк: ", summa )  # Output should be 99
