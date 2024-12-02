def read_data() -> list[list[int]]:
    with open('input_data.txt', 'r') as file:
        result = [list(map(int, row.strip().split())) for row
                  in file.readlines()]
    return result


input_data = read_data()


def is_secure(row: list[int]) -> bool:
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row) - 1):
            if not 1 <= abs(row[i] - row[i + 1]) <= 3:
                return False
        return True
    return False


def solution(data: list[list[int]]) -> int:
    # count = 0
    # for row in data:
    #     if is_secure(row):
    #         count += 1
    # return count
    return sum([is_secure(row) for row in data])


print(solution(input_data))
