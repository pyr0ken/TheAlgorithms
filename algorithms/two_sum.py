"""
    [2, 4, 5, 6, 7, 8, 9], 11 => [3, 4]
"""

def two_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]

        if s == target:
            return [p1+1 , p2+1]
        elif s > target:
            p2 -= 1
        else:
            p1 += 1

print(two_sum([2, 4, 5, 6, 7, 8, 9], 9))