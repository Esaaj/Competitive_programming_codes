import time
class score():
    def __init__(self):
        self.valuelist=[0]*11
    def calculation(self,valuelist):
        total=0
        for _ in range(0,8):
            total+=valuelist[_]
        return total
    def insert_score(self,index,value,valuelist):
        if(valuelist[index-1]<value):
            valuelist[index-1]=value
testcase=int(input())
while(testcase):
    score_object=score()
    submissions=int(input())
    while(submissions):
        index,value=input().split(" ")
        score_object.insert_score(int(index),int(value),score_object.valuelist)
        submissions-=1
    print(score_object.calculation(score_object.valuelist))
    testcase-=1