length=int(input())
inputlist=[int(x) for x in input().split(" ")]
while(True):
    print(len(inputlist))
    mini=min(inputlist)
    templist=[]
    for a in inputlist:
        temp=a-mini
        if(temp!=0):
            templist.append(temp)
    inputlist=templist 
    if(len(templist)==0):
        break
