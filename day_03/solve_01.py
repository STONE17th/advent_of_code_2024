def read_data():
    with open('input_data.txt', 'r') as file:
        return file.read()


def solution():
    data = read_data()
    result = []
    for row in data.split('mul'):
        if row.startswith('('):
            index = 0
            coord = ['', '']
            for ch in row[1:10]:
                if ch.isdigit():
                    coord[index] += ch
                elif ch == ',':
                    index += 1
                if ch == ')' and index:
                    result.append(tuple(map(int, coord)))
                    break

    return sum([a * b for a, b in result])


print(solution())
