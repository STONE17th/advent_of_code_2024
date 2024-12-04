def read_data():
    with open('input_data.txt', 'r') as file:
        return list(map(lambda x: x.strip(), file.readlines()))


x_mas = [
    ['MM', 'SS'],
    ['MS', 'MS'],
    ['SS', 'MM'],
    ['SM', 'SM'],
]


# def solution():
#     data = read_data()
#     count = 0
#     for x in range(1, len(data) - 1):
#         for y in range(1, len(data[0]) - 1):
#             if data[x][y] == 'A':
#                 target = [
#                     data[x - 1][y - 1] + data[x - 1][y + 1],
#                     data[x + 1][y - 1] + data[x + 1][y + 1],
#                 ]
#                 if target in x_mas:
#                     count += 1
#     return count

# def solution():
#     data = read_data()
#     count = 0
#     for x in range(1, len(data) - 1):
#         for y in range(1, len(data[0]) - 1):
#             if data[x][y] == 'A':
#                 x_y = [data[x + ix][y + iy] for ix in (-1, 1) for iy in (-1, 1)]
#                 match [*x_y]:
#                     case ['M', 'M', 'S', 'S']:
#                         count += 1
#                     case ['M', 'S', 'M', 'S']:
#                         count += 1
#                     case ['S', 'S', 'M', 'M']:
#                         count += 1
#                     case ['S', 'M', 'S', 'M']:
#                         count += 1
#     return count

def solution():
    data = read_data()
    count = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data[0]) - 1):
            if data[x][y] == 'A':
                x_y = [data[x + ix][y + iy] for ix in (-1, 1) for iy in (-1, 1)]
                if ''.join(x_y) in ('MMSS', 'MSMS', 'SSMM', 'SMSM'):
                    count += 1
    return count


print(solution())
