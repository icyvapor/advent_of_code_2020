#====== not proud of this at all.. =====
def main():
    f = open(r"..\input_day8.txt")

    next_ins = 0
    acc = 0
    seen = []
    prgm = []
    for line in f.readlines():
        ins, val = line.split()
        prgm.append([ins, int(val)])

    while next_ins not in seen:
        seen.append(next_ins)
        ins, val = prgm[next_ins]

        if ins == 'jmp':
            next_ins += val
            continue

        if ins == 'acc':
            acc += val

        next_ins += 1

    t_seen = []
    last = 0

    #back-tracing
    while next_ins!= len(prgm):
        t_seen.clear()
        last = seen.pop()
        t_seen.append(last)

        # try applying fix.
        if prgm[last][0] == 'jmp':
            next_ins = last + 1
        elif prgm[last][0] == 'nop' and prgm[last][1] != 0:
            next_ins += prgm[last][1]

        while next_ins not in seen and next_ins not in t_seen:
            if next_ins == len(prgm): # terminates successfully
                break

            t_seen.append(next_ins)
            ins, val = prgm[next_ins]

            if ins == 'jmp':
                next_ins += val
                continue
            next_ins += 1

    print(last)

    next_ins = 0
    acc = 0
    while next_ins != len(prgm):
        ins, val = prgm[next_ins]
        if ins == 'acc':
            acc += val

        if next_ins == last:
            if ins == 'nop':
                next_ins += val
                continue
        else:
            if ins == 'jmp':
                next_ins += val
                continue
        next_ins += 1

    print(acc)

if __name__ == '__main__':
    main()