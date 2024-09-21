numbers = tuple(map(float, input().split()))
set_numbers = set()

for i in numbers:
    if i not in set_numbers:
        print(f'{i:.1f} - {numbers.count(i)} times')
        set_numbers.add(i)