def check_presence(valuelist,checker):
    for a in valuelist:
        if a in checker:
            return 0
            break
    return 1

numbers = list("0123456789")
lower_case = list("abcdefghijklmnopqrstuvwxyz")
upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_characters = list("!@#$%^&*()-+")
flag = 0
length = int(input())
input_list = list(input())
flag += check_presence(input_list,numbers)
flag += check_presence(input_list,lower_case)
flag += check_presence(input_list,upper_case)
flag += check_presence(input_list,special_characters)
if(len(input_list)<6):
    if (6 - len(input_list) < flag):
        print(flag)
    else:
        print(6 - len(input_list))
else :
    print(flag)


