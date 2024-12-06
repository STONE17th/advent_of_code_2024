from copy import deepcopy

direct = (
    (-1, 0, '^'),
    (0, 1, '>'),
    (1, 0, 'v'),
    (0, -1, '<'),
)


def read_data():
    with open('input_data.txt', 'r') as file:
        return [list(row.strip()) for row in file.readlines()]


def go_play(data_map: list[list], x: int, y: int, need_map: bool = False):
    d = 0
    len_x, len_y = len(data_map), len(data_map[0])
    while True:
        n_x, n_y = x + direct[d][0], y + direct[d][1]
        if 0 <= n_x < len_x and 0 <= n_y < len_y:
            cell = data_map[n_x][n_y]
            if cell != '#':
                mark = direct[d][2]
                if cell in ('^', '<', '>', 'v'):
                    if cell == direct[d][2]:
                        return 1
                data_map[n_x][n_y] = mark
                x, y = n_x, n_y
            else:
                d = (d + 1) % len(direct)
        else:
            return 0


def solution():
    original_map = read_data()
    map_data = deepcopy(original_map)
    count = 0
    s_x, s_y = 0, 0
    for i in range(len(map_data)):
        if '^' in map_data[i]:
            s_x, s_y = i, map_data[i].index('^')
    for ix in range(len(map_data)):
        for iy in range(len(map_data[0])):
            map_data = deepcopy(original_map)
            if map_data[ix][iy] not in ('#', '^'):
                map_data[ix][iy] = '#'
            else:
                continue
            count += go_play(map_data, s_x, s_y)
    return count


print(solution())
