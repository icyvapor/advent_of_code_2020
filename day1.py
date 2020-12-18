f = open("input.txt")
numbers = set()
for line in f.readlines():
    numbers.add(int(line))

done = False

for i in numbers:
    s1 = 2020 - i
    for j in numbers:
        if j != i and (s1-j in numbers):
            print(i, j, s1-j)
            print(i*j*s1-j)
            done =True
            break
    if done:
        break
