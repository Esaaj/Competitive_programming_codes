test_case = int(input())
while(test_case):
    answer = 0
    count = [0]*26
    input_list = list(input())
    for a in input_list:
        count[int(ord(a)-97)] += 1
    for a in count:
        if(a>0):
            answer += 1
    print(answer)
    test_case -= 1

