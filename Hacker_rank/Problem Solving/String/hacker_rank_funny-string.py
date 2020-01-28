def count(valuelist):
    return_list = []
    for a in range(0,len(valuelist)-1):
        return_list.append(abs(valuelist[a]-valuelist[a+1]))
    return return_list
test_case = int(input())
while(test_case):
    input_list = list(input())
    reversed_input_list = reversed(input_list)
    input_list = [ord(x) for x in input_list]
    reversed_input_list = [ord(x) for x in reversed_input_list]
    input_list = count(input_list)
    reversed_input_list = count(reversed_input_list)
    if(input_list == reversed_input_list):
        print("Funny")
    else:
        print("Not Funny")
    test_case -= 1