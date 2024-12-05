from collections import defaultdict


def read_data():
    with open('input_data.txt', 'r') as file:
        indexes = []
        while True:
            line = file.readline().strip()
            if line:
                indexes.append(tuple(map(int, line.split('|'))))
            else:
                break
        rules = [list(map(int, line.split(','))) for line in file.readlines()]
        return indexes, rules


def solution():
    result = 0
    indexes, rules = read_data()
    dict_ind = defaultdict(list)
    for key, value in indexes:
        dict_ind[key].append(value)
    for rule in rules:
        is_wrong = False
        while True:
            start = True
            for cur_item in rule:
                for item_list in dict_ind[cur_item]:
                    if item_list in rule:
                        cur_ind = rule.index(cur_item)
                        nxt_ind = rule.index(item_list)
                        if cur_ind > nxt_ind:
                            is_wrong = True
                            rule[cur_ind], rule[nxt_ind] = rule[nxt_ind], rule[cur_ind]
                            start = False
            if start:
                break
        if is_wrong:
            result += rule[len(rule) // 2]
    return result


print(solution())
