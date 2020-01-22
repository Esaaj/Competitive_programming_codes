length, jump=[int(x) for x in input().split(" ")]
inputlist=[int(x) for x in input().split(" ")]
start=0
answer=100
while(True):
    if(start+jump>=length):
        start=-((start+jump)-length)
    start=start+jump
    if(inputlist[start]):
        answer-=3
    else:
        answer-=1
    if(start==0):
        print(answer)
        break