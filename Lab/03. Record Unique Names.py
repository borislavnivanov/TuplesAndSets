n = int(input())

set_names = set()

for _ in range(n):
    set_names.add(input())

print(*set_names, sep='\n')