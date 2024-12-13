def read_data(path: str):
    data = {}
    with open(path, 'r') as file:
        puzzle = 1
        flag = True
        while flag:
            data[puzzle] = {
                'a': tuple(map(int, file.readline()[12:].strip().split(', Y+'))),
                'b': tuple(map(int, file.readline()[12:].strip().split(', Y+'))),
                'r': tuple(map(int, file.readline()[9:].strip().split(', Y='))),
            }
            separator = file.readline()
            if separator:
                puzzle += 1
            else:
                flag = False
    return data


def solve_puzzle(a: tuple[int, int], b: tuple[int, int], r: tuple[int, int]) -> int:
    count_b = (r[0] * a[1] - r[1] * a[0]) / (b[0] * a[1] - b[1] * a[0])
    count_a = (r[0] - count_b * b[0]) / a[0]
    if int(count_a) == count_a and int(count_b) == count_b:
        return int(3 * count_a + count_b)
    return 0


def solution(path: str) -> int:
    result = 0
    puzzles = read_data(path)
    for puzzle in puzzles.values():
        result += solve_puzzle(**puzzle)
    return result


print(solution('input_data.txt'))
