'''
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
'''
test_case = int(input())
while(test_case):
    input_list = list(input())
    a = 0
    answer = 0
    flag = input_list[0]
    while(a<len(input_list)-1):
        if(input_list[a] == flag):
            while(True):
                a += 1
                if(a>len(input_list)-1):
                    break
                elif(input_list[a] != flag):
                    if(flag == 'A'):                    
                        flag = 'B'
                    else:
                        flag = 'A'
                    break
                else:
                    answer += 1
    test_case -= 1
    print(answer)