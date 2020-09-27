import itertools as it

size = int(input("Enter the size of list: "))
l = []
for i in range(size):
    l.append(int(input()))

print("original particles %s" % l)

_min = min(l)

def Find(l):
    k = l.copy()
    for i in it.combinations(l, 2):
        temp = abs(i[0] - i[1])
        print("size : %s"%temp)
        if _min > temp:
            _min = temp
            k.append(_min)

    Find(k)

  
print("min size of particles %s" % Find(l))
