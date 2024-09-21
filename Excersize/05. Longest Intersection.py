n = int(input())
longest = set()

for _ in range(n):
    range_1, range_2 = input().split('-')
    part_1 = [int(x) for x in range_1.split(',')]
    part_2 = [int(x) for x in range_2.split(',')]
    set_1 = set(x for x in range(part_1[0], part_1[1] + 1))
    set_2 = set(x for x in range(part_2[0], part_2[1] + 1))
    if len(longest) <= len(set_1.intersection(set_2)):
        longest = set_1.intersection(set_2)

print(f"Longest intersection is {list(longest)} with length {len(longest)}")