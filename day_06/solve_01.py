def read_data():
    with open('input_data.txt', 'r') as file:
        return [list(row.strip()) for row in file.readlines()]


def solution():
    map_data = read_data()
    direct = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )
    x, y = 0, 0
    for i in range(len(map_data)):
        if '^' in map_data[i]:
            x = i
            y = map_data[i].index('^')
    d = 0
    while True:
        n_x, n_y = x + direct[d][0], y + direct[d][1]
        try:
            cell = map_data[n_x][n_y]
        except:
            break
        else:
            if cell != '#':
                map_data[n_x][n_y] = '1'
                x, y = n_x, n_y
            else:
                d = (d + 1)%len(direct)

    return ''.join([''.join(row) for row in map_data]).count('1')
    # print(*map_data, sep='\n')


print(solution())
