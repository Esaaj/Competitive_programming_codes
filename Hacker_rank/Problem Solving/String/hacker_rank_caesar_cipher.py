qw = int(input())
input_list = list(input())
length = int(input())
if(length > 26):
    length = length % 26
answer = []
for a in input_list:
    ascii_value = ord(a)
    if(ascii_value>96 and ascii_value <123):
        if(ascii_value+length>122):
            temp = ascii_value+length - 122
            answer.append(chr(96 + temp))
        else:
            answer.append(chr(ascii_value+length))
    elif(ascii_value>64 and ascii_value <91):
        if(ascii_value+length>90):
            temp = ascii_value+length - 90
            answer.append(chr(64 + temp))
        else:
            answer.append(chr(ascii_value+length))
    else:
        answer.append(a)
answer_str = "" 
print(answer_str.join(answer)) 

