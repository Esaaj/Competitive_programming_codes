test_case = int(input())
while(test_case):
    input_list = list(input())
    length = len(input_list)
    checker = list("hackerrank")
    flag = 0
    count = 0
    for a in checker:
        while(flag < length):
            if(a == input_list[flag]):
                count += 1
                flag += 1
                break
            else:
                flag += 1
    if(count == 10):
        print("YES")
    else:
        print("NO")
    test_case -= 1

