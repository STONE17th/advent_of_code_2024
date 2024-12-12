def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip().split()


def calculate_stone(slot: str | int, depth: int, count_blinks: int):
    if slot == '0':
        data = ['1']
    elif not len(slot) % 2:
        len_stone = len(slot) // 2
        l_stone, r_stone = slot[:len_stone], slot[len_stone:]
        data = [l_stone, str(int(r_stone))]
    else:
        data = [str(int(slot) * 2024)]
    if depth < count_blinks:
        result = 0
        for slot in data:
            result += calculate_stone(slot, depth + 1, count_blinks)
        print(result)
        return result
    else:
        return len(data)


def solution(path: str, blink_count: int):
    stones = read_data(path)
    total_stones = 0
    for stone in stones:
        print(stone)
        total_stones += calculate_stone(stone, 1, blink_count)
    return total_stones


print(solution('input_data.txt', 25))
