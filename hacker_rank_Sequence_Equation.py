length=int(input())
inputlist=[int(x) for x in input().split(" ")]
for a in range(1,length+1):
    print(inputlist.index(inputlist.index(a)+1)+1)