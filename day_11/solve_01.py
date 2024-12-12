def read_data(path: str):
    with open(path, 'r') as file:
        return file.read().strip().split()


def solution(path: str, blink_count: int):
    stones = read_data(path)
    for _ in range(blink_count):
        i = 0
        while i < len(stones):
            if stones[i] == '0':
                stones[i] = '1'
                i += 1
            elif not len(stones[i]) % 2:
                len_stone = len(stones[i])//2
                l_stone, r_stone = stones[i][:len_stone], stones[i][len_stone:]
                stones[i] = l_stone
                stones.insert(i + 1, str(int(r_stone)))
                i += 2
            else:
                stones[i] = str(int(stones[i]) * 2024)
                i += 1
    return len(stones)


print(solution('input_data.txt', 25))