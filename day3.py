
def count_trees(elev_map, x_inc, y_inc):

    h = len(elev_map)
    w = len(elev_map[0]) -1
    print(h, w)
    tree_count = 0
    x = 0
    y = 0
    while x < h:
        if elev_map[x][y] == "#":
            tree_count += 1
        x = x + x_inc
        y = (y + y_inc) % w
    return tree_count

def main():
    f = open("input_day3.txt")
    elev_map = [x for x in f.readlines()]
    res = 1
    res *= count_trees(elev_map, 1, 1)
    res *= count_trees(elev_map, 1, 3)
    res *= count_trees(elev_map, 1, 5)
    res *= count_trees(elev_map, 1, 7)
    res *= count_trees(elev_map, 2, 1)

    print(res)

if __name__ == '__main__':
    main()