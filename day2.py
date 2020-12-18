
def count_valid():
    f = open("input_day2.txt")
    c = 0
    for line in f.readlines():
        frq, ltr, pswd = line.split()
        minmax = [int(x) for x in frq.split('-')]
        ltr = ltr[0]
        h = 0
        if len(pswd) >= minmax[0] and pswd[minmax[0]-1] == ltr:
            h += 1
        if len(pswd) >= minmax[1] and pswd[minmax[1]-1] == ltr:
            h += 1
        if h == 1:
            c += 1

    print(c)

if __name__ == '__main__':
    count_valid()