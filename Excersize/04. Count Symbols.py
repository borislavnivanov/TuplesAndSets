text = tuple(sorted([char for char in input()]))

set_of_letters = set()
for elem in text:
    set_of_letters.add(elem)

for sym in sorted(set_of_letters):
    print(f'{sym}: {text.count(sym)} time/s')