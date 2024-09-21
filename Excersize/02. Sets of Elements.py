n, m = (int(x) for x in (input().split()))

duplicated_elements = set()

set_n = set()
set_m = set()

for _ in range(n):
    set_n.add(input())

for _ in range(m):
    set_m.add(input())

duplicated_elements=set_n.intersection(set_m)

print(*duplicated_elements, sep='\n')