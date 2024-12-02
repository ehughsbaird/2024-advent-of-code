with open("input.txt", "r") as file:
    left = []
    right = []
    for line in file.readlines():
        line = line[:-1]
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    left = sorted(left)
    right = sorted(right)
    # len(left) == len(right)
    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(left[i] - right[i])
    print(total_dist)


