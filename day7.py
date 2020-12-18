import re

#=== Part 1 ======
def parse_rule(txt, lut, contain_rules, pack_rules):
    res = re.findall(r"(^\b.+?\b|(?<=\d\s)\b.+?\b) bags?", txt)
    for c in res:
        if c not in lut:
            lut[c] = len(lut)

    if len(res) == 1:
        return

    current_color = lut[res[0]]
    for c in res[1:]:
        if lut[c] not in contain_rules:
            contain_rules[lut[c]] = set()
        contain_rules[lut[c]].add(current_color)

    counts = re.findall(r"(\d+) \b.+?\b bags?", txt)
    current_rule = {}
    for c, n in zip(res[1:], counts):
        current_rule[lut[c]] = int(n)

    pack_rules[current_color] = current_rule


def count_color(target, rules, contain_list):
    if target not in rules:
        return

    for c in rules[target]:
        if c not in contain_list:
            contain_list.add(c)
            count_color(c, rules, contain_list)

    return

def pack_bags(target, pack_rules):
    if target not in pack_rules:
        return 0

    sum = 0
    for p in pack_rules[target]:
        sum += pack_rules[target][p] * (1 + pack_bags(p, pack_rules))

    return sum

def main():
    f = open("input_day7.txt")

    color_lut = {}
    contain_rules = {}
    pack_rules = {}
    for line in f.readlines():
        parse_rule(line, color_lut, contain_rules, pack_rules)

    contain_list = set()
    count_color(color_lut["shiny gold"], contain_rules, contain_list)
    print(len(contain_list))

    # part 2
    total_num = pack_bags(color_lut["shiny gold"], pack_rules) + 1
    print("total ", total_num )

if __name__ == '__main__':
    main()