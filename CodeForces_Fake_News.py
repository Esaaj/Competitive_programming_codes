input_list=list(input())
flag=0
for a in input_list:
    if(a=='h' and flag==0):
        flag=1
    elif(a=='e' and flag==1):
        flag=2
    elif(a=='i' and flag==2):
        flag=3
    elif(a=='d' and flag==3):
        flag=4
    elif(a=='i' and flag==4):
        flag=5
if(flag==5):
    print("YES")
else:
    print("NO")