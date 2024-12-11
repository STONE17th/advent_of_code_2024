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
    new_data = []
    row = [data_ext[0]]
    for i in range(1, len(data_ext)):
        if row[-1] == data_ext[i]:
            row.append(data_ext[i])
        else:
            new_data.append(row)
            row = [data_ext[i]]
    new_data.append(row)
    i_digit = len(new_data) - 1
    while i_digit >= 0:
        i_dots = 0
        while i_dots < len(new_data):
            shift = 0
            if i_digit < i_dots:
                break
            if new_data[i_dots][0] == '.' and len(new_data[i_digit]) <= len(new_data[i_dots]):
                len_digits = len(new_data[i_digit])
                len_dots = len(new_data[i_dots])

                difference = len_dots - len_digits
                new_data[i_dots] = new_data[i_digit].copy()
                if difference:
                    new_data.insert(i_dots + 1, ['.'] * difference)
                    shift = 1
                new_data[i_digit + shift] = ['.'] * len_digits
                break

            i_dots += 1
        i_digit -= 1
    print(new_data)
    return sum([i * int(item) for i, item in enumerate(chain(*new_data)) if item != '.'])


print(solution('input_data.txt'))
