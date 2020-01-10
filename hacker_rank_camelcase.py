alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
input_list=list(input())
answer=1
for a in input_list:
    if a in alpha:
        answer+=1
print(answer)
