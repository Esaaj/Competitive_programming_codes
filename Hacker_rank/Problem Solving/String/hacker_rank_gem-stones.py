test_case = int(input())
checker = 0
alpha = list("abcdefghijklmnopqrstuvwxyz")
count = [0] * 26
answer = 0
while(checker < test_case):
    inputlist = list(input())
    for b in range(0,26):
        if alpha[b] in inputlist:
            count[b] += 1
    checker += 1
    for temp in range(0,26):
        if(count[temp] > checker):
            count[temp] = checker
        if(count[temp] == test_case):
            answer += 1
print(answer)
 