import math

n = int(input())
even_set, odd_set = set(), set()

for i in range(1, n + 1):
    name = math.floor(sum([ord(x) for x in input()]) / i)
    if name % 2 != 0:
        odd_set.add(name)
    else:
        even_set.add(name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')