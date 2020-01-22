input_str=input()
input_str=input_str.lower()
answer=[]
answer.append('.')
for a in input_str:
    if a in ["a", "o", "y", "e", "u", "i"]:
        pass
    else: 
        answer.append(a)
        answer.append('.')
str_answer=''
del answer[len(answer)-1]
for _ in answer:
    str_answer = str_answer + str(_)    
print(str_answer)
