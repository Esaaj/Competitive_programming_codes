once_code=[0,1,11,111,1111,11111,111111,1111111,11111111,111111111]
length=int(input())
for a in range(0,length):
    answer=0
    input_int=int(input())
    loop_var=1
    while(loop_var<=input_int):
        digit_length=len(str(loop_var))
        if(loop_var%once_code[digit_length]==0):
            answer+=1
            loop_var+=once_code[digit_length]
        else:
            loop_var+=1
    print(answer)
'''  for _ in range(1,input_int+1):
        digit_length=len(str(_))
        if(_%once_code[digit_length]==0):
            answer+=1
    '''