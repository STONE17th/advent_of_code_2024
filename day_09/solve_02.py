from itertools import chain

from itertools import chain


class Cell:

    def __init__(self, data: str | bool):
        self.data = data

    def __repr__(self):
        return self.data if self.data else '.'


class Section:
    section_id = 0

    def __init__(self, section_id: str, count: int):
        self.id = str(section_id)
        self.count = count
        self.section = [Cell(self.id) for _ in range(self.count)]

    def __repr__(self):
        return ''.join(map(str, self.section))

    def __copy__(self):
        instance = Section(self.id, self.count)
        return instance

    def __len__(self):
        return len(self.section)


class DiskMap:
    section_id = 0

    def __init__(self, path: str):
        with open(path, 'r') as file:
            data = file.read().strip()
        self.map = []
        for i, item in enumerate(data):
            if int(item):
                if not i % 2:
                    data = DiskMap.section_id
                    DiskMap.section_id += 1
                else:
                    data = ''
                self.map.append(Section(data, int(item)))

    def list_disk(self) -> list[Cell]:
        return list(chain(*[section.section for section in self.map]))

    def swap_section(self, data_id: int, empty_id: int):
        data_section = self.map.copy()[data_id]
        empty_section = self.map.copy()[empty_id]
        len_data = len(data_section)
        len_empty = len(empty_section)
        difference = len_data - len_empty
        self.map[data_id] = empty_section
        self.map[empty_id] = Section('', len_empty)
        shift = True
        if difference:
            new_section = Section('', difference)
            self.map.insert(data_id + 1, new_section)
            shift = False
        return shift

    def sum_cells(self):
        result = 0
        k = 0
        for section in self.map:
            for cell in section.section:
                if cell.data:
                    result += int(cell.data) * k
                k += 1
        return result

    def __str__(self):
        return ''.join(map(str, self.map))


def solution(path: str):
    disk_map = DiskMap(path)
    ife = len(disk_map.map) - 1
    while ife >= 0:
        ifs = 0
        if disk_map.map[ife].id:
            while ifs < ife:
                if (not disk_map.map[ifs].id) and (len(disk_map.map[ifs]) >= len(disk_map.map[ife])):
                    if disk_map.swap_section(ifs, ife):
                        ife -= 1
                    break
                else:
                    ifs += 1
            else:
                ife -= 1
                ifs += 1
        else:
            ife -= 1
    return disk_map.sum_cells()


print(solution('input_data.txt'))
