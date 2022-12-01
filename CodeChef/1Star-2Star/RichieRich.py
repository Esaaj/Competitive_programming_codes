testCase = int(input())

for _ in range(0, testCase):
    A, B, X = [int(x) for x in input().split(" ")]
    difference = B - A
    timeToReach = difference/X
    print(int(timeToReach))