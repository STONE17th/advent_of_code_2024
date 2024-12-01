def read_data():
    with open('input_data.txt', 'r') as file:
        data = file.readlines()
    data = [row.split() for row in data]
    first_data = []
    second_data = []
    for item in data:
        first_data.append(int(item[0]))
        second_data.append(int(item[1]))
    return first_data, second_data


first_list, second_list = read_data()


def solve(first, second):
    result = []
    for item in first:
        result.append(item * second.count(item))
    return sum(result)


print(solve(first_list, second_list))
