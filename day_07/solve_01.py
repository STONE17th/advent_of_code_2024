from itertools import product


# def all_combinations(any_list):
#     return chain(*map(lambda x: combinations(any_list, x), range(0, len(any_list) + 1)))


def read_data(path):
    with open(path, 'r') as file:
        data = [row.strip().split(': ') for row in file.readlines()]

    return [(row[0], tuple(row[1].split())) for row in data]


def solution(path: str) -> int:
    operations = ('+', '*')
    input_data = read_data(path)
    result = 0
    for answer, args in input_data:
        count_operations = len(args) - 1
        operators = tuple(product(operations, repeat=count_operations))
        for item in operators:
            pattern = args[0]
            for i in range(len(item)):
                pattern = str(eval(pattern + item[i] + args[i + 1]))
            if pattern == answer:
                result += int(pattern)
                break
    return result


print(solution('input_data.txt'))
