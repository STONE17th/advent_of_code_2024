import re


def read_data():
    with open('input_data.txt', 'r') as file:
        return file.read()


input_data = read_data()


def do_or_dont(data: str) -> str:
    clean_data = data.split("don't()")
    out_data = [clean_data.pop(0)]
    for row in clean_data:
        temp_row = row.split('do()')
        if len(temp_row) > 1:
            for item in temp_row[1:]:
                out_data.append(item)
    return ''.join(out_data)


def solution(data: str):
    new_data = do_or_dont(data)
    result = []
    for row in new_data.split('mul'):
        if row.startswith('('):
            index = 0
            coord = ['', '']
            for ch in row[1:10]:
                if ch.isdigit():
                    coord[index] += ch
                elif ch == ',':
                    index += 1
                if ch == ')' and index:
                    result.append(tuple(map(int, coord)))
                    break
    return sum([a * b for a, b in result])


print(solution(input_data))
#
# pattern = r'mul\(\d{1,3},\d{1,3}\d\)'
# result = re.findall(pattern, input_data)
# print(sum(map(lambda x: int(x[0]) * int(x[1]), [item[4:-1].split(',') for item in result])))
