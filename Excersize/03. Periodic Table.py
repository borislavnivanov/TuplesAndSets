n = int(input())

elements = set()

for _ in range(n):
    [elements.add(elem) for elem in (input().split())]

print(*elements, sep='\n')