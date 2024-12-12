def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip().split()

cast

def solution(path: str, blink_count: int):
    stones = read_data(path)
    for k in range(blink_count):
        print(k)

    return len(stones)


print(solution('input_data.txt', 75))