def main():
    f = open(r"..\input_day9.txt")

    current = 0
    n = 25
    prev = []
    all_nums = []
    check_set = set()
    for line in f.readlines():
        current = int(line)
        if len(prev) < n:
            prev.append(current)
            check_set.add(current)
            continue

        valid = False
        for i in prev:
            other = current - i
            if other != i and other in check_set:
                valid = True
                break

        if valid:
            forget_num = prev.pop(0)
            check_set.discard(forget_num)
            all_nums.append(forget_num)
            prev.append(current)
            check_set.add(current)
        else:
            print("Invalid number: {}".format(current))
            break


    # part 2
    all_nums.extend(prev)
    dp_table = []
    for j in range(1, len(all_nums)):
        for i in range(j):
            if len(dp_table) == i:
                #row doesn't exist
                cur_sum = all_nums[i] + all_nums[j]
                if cur_sum == current:
                    # sequence only have 2 elements, which sums to the invalid number
                    print("Weakness: {}".format(current))
                    return
                # add new row and record
                dp_table.append([cur_sum])
            else:
                cur_sum = dp_table[i][j-i-2] + all_nums[j]
                if cur_sum == current:
                    # sequence found! Compute weakness
                    wkns_max = max(all_nums[i:j+1])
                    wkns_min = min(all_nums[i:j+1])
                    print("Weakness: {}".format(wkns_max + wkns_min))
                    return
                dp_table[i].append(cur_sum)

    print("Fail!") # should never reach here.


if __name__ == '__main__':
    main()