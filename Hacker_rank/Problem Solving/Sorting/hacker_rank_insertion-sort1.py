length = input()
input_list = input().split(" ")
checker = int(input_list[len(input_list)-1])
for a in range(len(input_list)-2,-2,-1):
    if(a == -1):
        input_list[0] = str(checker)
        answer = " "
        answer = answer.join(input_list)
        print(answer)
        break
    elif(int(input_list[a])>int(checker)):
        input_list[a+1] = input_list [a]
        answer = " "
        answer = answer.join(input_list)
        print(answer)
    else:
        input_list[a + 1] = str(checker)
        answer = " "
        answer = answer.join(input_list)
        print(answer)
        break
    