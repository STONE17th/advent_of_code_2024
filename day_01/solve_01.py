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


first_list, second_first = read_data()


def solve(first, second):
    first.sort(reverse=True)
    second.sort(reverse=True)
    result = []
    for _ in range(len(first)):
        result.append(abs(first.pop() - second.pop()))
    return sum(result)


print(solve(first_list, second_first))
