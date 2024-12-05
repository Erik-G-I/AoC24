l0 = [int(x) for x in open(file="input.txt", mode="r").read().split()]
l1 = sorted(l0[::2])
l2 = sorted(l0[1::2])
print(sum([abs(y - x) for (x, y) in list(zip(l1, l2))]))

l1_1 = [x * l2.count(x) for x in l1]
print(sum(l1_1))