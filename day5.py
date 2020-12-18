def to_id(seat_code):
    id = 0
    seat_code = seat_code[:-1]
    for c in seat_code:
        id = id << 1
        if c == 'B' or c == 'R':
            id += 1

    return id

def main():
    f = open("input_day5.txt")
    highest = -1
    lowest = 850
    cur_id = 0
    actual_sum = 0
    for seat_code in f.readlines():
        cur_id = to_id(seat_code)
        if highest < cur_id:
            highest = cur_id
        if lowest > cur_id:
            lowest = cur_id
        actual_sum += cur_id

    count = highest - lowest + 1
    res = (highest + lowest) * count / 2 - actual_sum
    print(res)

if __name__ == '__main__':
    main()