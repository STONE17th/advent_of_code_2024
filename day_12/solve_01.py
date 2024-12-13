from collections import defaultdict


class Cell:

    def __init__(self, plant: str, x: int, y: int):
        self.plant = plant
        self.x = x
        self.y = y

    def __repr__(self):
        return self.plant

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f'{self.x}{self.y}{self.plant}')


class Map:
    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = [row.strip() for row in file.readlines()]
        self.map = []
        for x, row in enumerate(data):
            data_row = []
            for y, plant in enumerate(row):
                data_row.append(Cell(plant, x, y))
            self.map.append(data_row)

    def show(self, target_plant: str | bool = False):
        for row in self.map:
            for cell in row:
                if target_plant:
                    plant = cell.plant if cell.plant == target_plant else '.'
                else:
                    plant = cell.plant
                print(plant, end='')
            print()


class Section:
    sections = defaultdict(list)
    DIRECT = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    )

    def __init__(self, garden_map: Map, start_cell: Cell):
        self.garden_map = garden_map.map
        self.plant = start_cell.plant
        self._map = [start_cell]
        self.plot: list[Cell] = [start_cell]
        self.plot_calculation()
        Section.sections[self.plant] += self.plot

    def plot_calculation(self):
        while self._map:
            cell = self._map.pop(0)
            for xd, yd in Section.DIRECT:
                nx, ny = cell.x + xd, cell.y + yd
                if 0 <= nx < len(self.garden_map) and 0 <= ny < len(self.garden_map[0]):
                    n_cell = self.garden_map[nx][ny]
                    if self.plant == n_cell.plant and n_cell not in self.plot:
                        self._map.append(n_cell)
                        self.plot.append(n_cell)

    def area(self):
        return len(self.plot)

    def perimetr(self):
        result = 0
        for cell in self.plot:
            for xd, yd in Section.DIRECT:
                nx, ny = cell.x + xd, cell.y + yd
                if 0 <= nx < len(self.garden_map) and 0 <= ny < len(self.garden_map[0]):
                    if self.garden_map[nx][ny].plant != self.plant:
                        result += 1
                else:
                    result += 1
        return result


def solution(path: str):
    garden = Map(path)
    sections = []
    for x in range(len(garden.map)):
        for y in range(len(garden.map[0])):
            cell = garden.map[x][y]
            if not (cell.plant in Section.sections and cell in Section.sections[cell.plant]):
                sections.append(Section(garden, cell))
    #
    # for section in sections:
    #     print(section.plant, section.area(), section.perimetr())
    return sum([section.area() * section.perimetr() for section in sections])


print(solution('input_data.txt'))
