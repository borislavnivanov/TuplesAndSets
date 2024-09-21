n = int(input())

set_cars = set()

for _ in range(n):
    action, plate = input().split(', ')
    if action == 'IN':
        set_cars.add(plate)
    elif action == 'OUT':
        set_cars.remove(plate)

if set_cars:
    print(*set_cars, sep='\n')
else:
    print('Parking Lot is Empty')