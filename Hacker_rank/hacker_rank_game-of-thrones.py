string= input()
count = [0]*26
answer = 0
for a in string:
    count[int(ord(a)-97)] += 1
for a in count:
    if(a == 1):
        answer += 1
        if(answer == 2):
            print("No")
            exit()
print("Yes")