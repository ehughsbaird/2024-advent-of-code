with open("input.txt", "r") as file:
    left = []
    right = dict()
    for line in file.readlines():
        line = line[:-1]
        l, r = line.split()
        left.append(int(l))
        r = int(r)
        if r in right:
            right[r] += 1
        else:
            right[r] = 1

    score = 0
    for value in left:
        num = right[value] if value in right else 0
        score += value * num
    print(score)


