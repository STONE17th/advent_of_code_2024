class Cell:

    def __init__(self, value: str, x: int = -1, y: int = -1):
        self.value = int(value)
        self.x = x
        self.y = y
        self.neighbours = []
        self.paths = set()

    def __repr__(self):
        return f'{self.x} {self.y} {self.value}'

    def __str__(self):
        return f'{self.x} {self.y} {self.value}'

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash(f'{self.x}{self.y}{self.value}')


class Map:
    DIRECT = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )

    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = list(map(lambda x: x.strip(), file.readlines()))
            paths = [[Cell('-1')] * (len(data[0]) + 2)]
            paths += [[Cell(ch, x, y) for y, ch in enumerate(['-1'] + list(row) + ['-1'])] for x, row in
                      enumerate(data, 1)]
            paths += [[Cell('-1')] * (len(data[0]) + 2)]
        self.paths = paths
        self.list_starts = [cell for row in self.paths for cell in row if not cell.value]

    def gather_neighbors(self, x: int, y: int):
        cell = self.paths[x][y]
        for nx, ny in Map.DIRECT:
            next_cell = self.paths[cell.x + nx][cell.y + ny]
            if next_cell.value == cell.value + 1:
                cell.neighbours.append(next_cell)

    def walk(self):
        for start_cell in self.list_starts:
            current_path = [start_cell]
            while current_path:
                cell = current_path.pop(0)
                if cell.value == 9:
                    start_cell.paths.add(cell)
                else:
                    for nx, ny in Map.DIRECT:
                        next_cell = self.paths[cell.x + nx][cell.y + ny]
                        if next_cell.value == cell.value + 1:
                            current_path.append(next_cell)

    def show(self):
        for row in self.paths[1:-1]:
            print(row[1:-1])

    def total_paths(self):
        return sum([len(cell.paths) for row in self.paths for cell in row])


def solution(path: str):
    map_paths = Map(path)
    map_paths.walk()
    return map_paths.total_paths()


print(solution('input_data.txt'))
