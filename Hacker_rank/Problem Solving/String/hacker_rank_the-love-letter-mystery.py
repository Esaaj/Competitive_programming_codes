test_case = int(input())
while(test_case):
    string= input()
    count = [0]*26
    answer = 0
    for a in string:
        count[int(ord(a)-97)] += 1
    for a in count:
        if(a % 2 != 0):
            answer += 1
    if(answer != 0):
        if(answer%2 != 0):
            print(answer-1)
        else:
            print(answer)
    else:
        if(len(string)%2 != 0):
            print(len(string)-1)
        else:
            print(len(string))
    test_case -= 1

#Incomplete