def read_data() -> list[list[int]]:
    with open('input_data.txt', 'r') as file:
        result = [list(map(int, row.strip().split())) for row
                  in file.readlines()]
    return result


input_data = read_data()


def is_secure(row_data):
    i = 0
    sign = (row_data[i] - row_data[i + 1]) > 0
    for i in range(len(row_data) - 1):
        if ((row_data[i] - row_data[i + 1]) > 0) == sign:
            if 1 <= abs(row_data[i] - row_data[i + 1]) <= 3:
                continue
            return False
        return False
    return True


def solution(data: list[list[int]]) -> int:
    broken = [row for row in data if not is_secure(row)]
    norm_broken = 0
    for row in broken:
        for i in range(len(row)):
            row_copy = row.copy()
            row_copy.pop(i)
            if is_secure(row_copy):
                norm_broken += 1
                break
    return len(data) - len(broken) + norm_broken


print(solution(input_data))
