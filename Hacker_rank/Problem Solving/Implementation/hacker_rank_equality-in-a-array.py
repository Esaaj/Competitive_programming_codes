length = int(input())
input_list = [int(x) for x in input().split(" ")]
counter = [0]*100
for a in input_list:
    if(counter[a-1] == 0):
        counter[a-1] = input_list.count(a)
counter[counter.index(max(counter))] = 0
print(sum(counter))