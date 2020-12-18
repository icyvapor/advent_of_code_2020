
def main():
    f = open("input_day6.txt")
    sum = 0
    group_count = 0
    q = {}
    for line in f.readlines():
        if len(line) == 1:
            if len(q.keys()) > 0:
                for key in q:
                    if q[key] == group_count:
                        sum += 1
                q.clear()
                group_count = 0
            continue
        for c in line[:-1]:
            if c in q:
                q[c] += 1
            else:
                q[c] = 1
        group_count += 1
    if len(q.keys()) > 0:
        for key in q:
            if q[key] == group_count:
                sum += 1

    print(sum)

if __name__ == '__main__':
    main()