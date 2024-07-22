def calculate_structure_sum(data):
    def summa1(item):
        number = 0

        if isinstance(item, int):
            number += item
        elif isinstance(item, str):
            number += len(item)
        elif isinstance(item, (list, tuple, set)):
            for sub_item in item:
                number += summa1(sub_item)
        elif isinstance(item, dict):
            for key, value in item.items():
                number += summa1(key)
                number += summa1(value)
        elif isinstance(item, bool):
            number += int(item)

        return number

    return summa1(data)


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

summa = calculate_structure_sum(data_structure)
print("Подсчёт суммы всех чисел и длин всех строк: ", summa )
