from itertools import chain


class Cell:

    def __init__(self, data: bool, cell_id: int = 0):
        self.data = data
        self.id = cell_id

    def __repr__(self):
        return str(self.id) if self.data else '.'


class Section:
    section_id = 0

    def __init__(self, data: bool, count: str):
        self.count = int(count)
        self.data = data
        if data:
            self.data = Section.section_id
            Section.section_id += 1
        self.section = [Cell(data, self.data) for i in range(self.count)]

    def __repr__(self):
        return ''.join(map(str, self.section))


class DiskMap:
    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = file.read().strip()
        self.map = [Section(not bool(i % 2), item) for i, item in enumerate(data)]

    def list_disk(self) -> list[Cell]:
        return list(chain(*[section.section for section in self.map]))

    def __str__(self):
        return ''.join(map(str, self.map))


def solution(path: str):
    disk_map = DiskMap(path)
    list_disk = disk_map.list_disk()
    ife = len(list_disk) - 1
    for ifs in range(len(list_disk)):
        while not list_disk[ife].data:
            ife -= 1
        if ifs > ife:
            break
        if not list_disk[ifs].data:
            list_disk[ifs], list_disk[ife] = list_disk[ife], list_disk[ifs]
    return sum([cell.id * new_id for new_id, cell in enumerate(list_disk) if cell.data])


print(solution('input_data.txt'))
