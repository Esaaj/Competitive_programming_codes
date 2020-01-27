length = int(input())
input_list = list(input())
answer = 0
looper = 0
while(looper+3 <= length):
    string = ""
    string = string.join(input_list[looper:looper+3])
    if(string == '010'):
        answer += 1
        looper += 3
    else:
        looper += 1
print(answer)
