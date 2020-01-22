input_str = input()
repectation = len(input_str)/3
checker = ['S','O','S']
seperator = 0 
answer = 0
while (repectation):
    substring = list(input_str)[seperator:seperator+3]
    if(substring != checker):
        for a in range(0,3):
            if(checker[a] != substring[a]):
                answer += 1
    seperator += 3
    repectation -= 1
print(answer)
