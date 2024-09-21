n = int(input())

reservations = set()

for _ in range(n):
    reservations.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    reservations.remove(guest)

print(len(reservations))
print(*sorted(reservations), sep='\n')