length=int(input())
while(length):
    answer=0
    temp=int(input())
    inputlist=[int(x) for x in list(str(temp))]
    for a in inputlist:
        if(a==0):
            pass
        elif(temp%a==0):
            answer+=1
    print(answer)
    length-=1