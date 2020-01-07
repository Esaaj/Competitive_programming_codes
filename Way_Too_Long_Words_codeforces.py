length=int(input())
for a in range(0,length):
    str_received = input()
    answer=[]
    if(len(str_received)>10):
        answer.append(str_received[0])
        answer.append(len(str_received)-2)
        answer.append(str_received[len(str_received)-1])
        str_answer = ''
        for _ in answer:
            str_answer = str_answer + str(_)    
        print(str_answer)
    else:
        print(str_received)