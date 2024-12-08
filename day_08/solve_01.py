from collections import defaultdict


class Cell:
    antenna_xy = defaultdict(list)

    def __init__(self, x: int, y: int, antenna: str):
        self.x = x
        self.y = y
        self.name = antenna
        self.antinode = False
        if antenna != '.':
            Cell.antenna_xy[antenna].append((x, y))

    def __repr__(self):
        return '#' if self.antinode else '.'

    def __str__(self):
        if self.antinode:
            return '#'
        return self.name


class Table:

    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = [[Cell(x, y, cell) for y, cell in enumerate(row.strip())] for x, row in enumerate(file.readlines())]
        self.data = data

    def antinode(self, x: int, y: int):
        self.data[x][y].antinode = True

    def print(self):
        for row in self.data:
            print(''.join([str(cell) for cell in row]))

    def count_antinode(self):
        return sum([1 for row in self.data for cell in row if cell.antinode])

    def antinode_antennas(self):
        for antennas in Cell.antenna_xy.values():
            if len(antennas) > 1:
                for x, y in antennas:
                    self.data[x][y].antinode = True


def solution(path: str) -> int:
    table = Table(path)
    for row in table.data:
        for cell in row:
            if cell.name != '.':
                xa, ya = cell.x, cell.y
                for name, list_xy in Cell.antenna_xy.items():
                    for xy in list_xy:
                        if (name == cell.name) and ((xa, ya) != xy):
                            xaa, yaa = xy
                            xp, yp = xa - (xaa - xa), ya - (yaa - ya)
                            if (0 <= xp < len(table.data)) and (0 <= yp < len(table.data[0])):
                                table.antinode(xp, yp)

    return table.count_antinode()


print(solution('input_data.txt'))
