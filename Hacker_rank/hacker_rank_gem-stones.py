test_case = int(input())
checker = 0
alpha = list("abcdefghijklmnopqrstuvwxyz")
count = [0] * 26
while(checker < test_case):
    for a in list(input()):
        for b in range(0,26):
            if a is alpha[b]:
                count[b] += 1
    checker += 1
    for temp in range(0,26):
        if(count[temp] > checker):
            count[temp] = checker 
    print(count)
 