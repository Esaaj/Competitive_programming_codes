length=int(input())
input_list=[int(x) for x in input().split(" ")]
input_list=sorted(input_list)
check_len=length
start_len=0
flag=0
while(True):
    temp=int(check_len/2)
    if(True):
        if(input_list[temp-1]!=temp):
            del input_list[temp-1:check_len]
            check_len=temp
        else:
            del input_list[start_len:temp-1]
            check_len=len(input_list)
    else:
        for a in range(input_list[0],input_list[len(input_list)-1]):
            if a not in input_list:
                print(a)
                flag=1
        if(flag==0):
            print(input_list[len(input_list)-1]+1)
            
        break