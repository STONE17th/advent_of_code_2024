from itertools import chain


def read_data(path):
    with open(path, 'r') as file:
        return file.read().strip()


def solution(path: str):
    data = read_data(path)
    data_ext = []
    for i, item in enumerate(data):
        data_ext.append((i // 2 if not i % 2 else '.', int(item)))
    data_ext = list(chain(*[[str(item[0])] * item[1] for item in data_ext]))
    # print(data_ext)
    ife = len(data_ext) - 1
    for ifs in range(len(data_ext)):
        while not data_ext[ife].isdigit():
            ife -= 1
        if ifs > ife:
            break
        if data_ext[ifs] == '.':
            data_ext[ifs], data_ext[ife] = data_ext[ife], data_ext[ifs]

    print(''.join(data_ext))
    return sum([i * int(item) for i, item in enumerate(data_ext) if item.isdigit()])


print(solution('input_data.txt'))
