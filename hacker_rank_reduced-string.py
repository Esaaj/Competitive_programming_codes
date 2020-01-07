input_list=list(input())
a=0
while(a<len(input_list)-1):
    if(input_list[a]==input_list[a+1]):
        del input_list[a:a+2]
        a=0
        if(len(input_list)==0):
            print("Empty String")
            exit()
    else:
        a+=1
answer=''.join([str(elem) for elem in input_list]) 
print(answer)

    
