length=int(input())
for a in range(0,length):
    input_str=input()
    if(str(input_str[-2:])=="po"):
        print("FILIPINO")
    elif(str(input_str[-4:])=="desu" or str(input_str[-4:])=="masu"):
        print("JAPANESE")
    elif(str(input_str[-5:])=="mnida"):
        print("KOREAN")