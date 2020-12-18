def passport_valid(info):
    fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for f in fields:
        if f not in info:
            return False

    byr = int(info["byr"])
    if byr < 1920 or byr > 2002:
        return False

    iyr = int(info["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False

    eyr = int(info["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    hgt = info["hgt"]
    if hgt[-2:] == "cm":
        val = int(hgt[:-2])
        if val < 150 or  val > 193:
            return False
    elif hgt[-2:] == "in":
        val = int(hgt[:-2])
        if val < 59 or  val > 76:
            return False
    else:
        return False

    hcl = info["hcl"]
    if hcl[0]!= '#' or len(hcl) != 7:
        return False
    for i in range(1, 7):
        if (hcl[i] >= '0' and hcl[i] <= '9') or\
                (hcl[i] >= 'a' and hcl[i] <= 'f'):
            continue
        else:
            return False

    if info["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    pid = info["pid"]
    if len(pid)!= 9:
        return False
    for c in pid:
        if c <'0' or c>'9' :
            return False

    return True

def main():
    f = open("input_day4.txt")
    valid_count = 0
    cur_info = {}
    for rec_line in f.readlines():
        if len(rec_line) == 1:
            if len(cur_info.items()) > 0:
                if passport_valid(cur_info):
                    valid_count += 1
                cur_info.clear()
        else:
            #parsing info
            for entry in rec_line.split():
                key, val = entry.split(":")
                cur_info[key] = val

    print(valid_count)

if __name__ == '__main__':
    main()