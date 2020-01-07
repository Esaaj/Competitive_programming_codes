class summultiply(object):
    def __init__(self):
        inputlist=[]
    def calculation(self,a,b):
        if(int(a)+int(b)==int(a)*int(b)):
            return True
        else:
            return False
    def rotation(self,valuelist):
        listlen=len(valuelist)
        answercount=0
        for a in range(0,listlen-1):
            for b in range(a+1,listlen):
                if(self.calculation(valuelist[a],valuelist[b])):
                    answercount+=1
        return answercount
testcase=int(input())
while(testcase):
    classobj=summultiply()
    a=input()
    inputstr=input()
    classobj.inputlist=inputstr.split(" ")
    print(classobj.rotation(classobj.inputlist))
    testcase-=1