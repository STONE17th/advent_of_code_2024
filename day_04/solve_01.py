def read_data():
    with open('input_data.txt', 'r') as file:
        data = list(map(lambda x: x.strip(), file.readlines()))
    result = ['.' * (len(data[0]) + 2)]
    for row in data:
        result.append('.' + row + '.')
    result.append('.' * (len(data[0]) + 2))
    return result


directions = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x, y) != (0, 0)]


def solution():
    data = read_data()
    count = 0
    for x in range(1, len(data[0]) - 1):
        for y in range(1, len(data) - 1):
            if data[x][y] == 'X':
                for in_x, in_y in directions:
                    mx, my = x + in_x, y + in_y
                    ax, ay = x + 2 * in_x, y + 2 * in_y
                    sx, sy = x + 3 * in_x, y + 3 * in_y
                    if data[mx][my] == 'M' and data[ax][ay] == "A" and data[sx][sy] == "S":
                        count += 1
    return count


print(solution())
