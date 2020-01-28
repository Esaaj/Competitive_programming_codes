string_one = input()
string_two = input()
count_one = [0]*26
count_two = [0]*26
answer = 0
for a in string_one:
    count_one[int(ord(a)-97)] += 1
for a in string_two:
    count_two[int(ord(a)-97)] += 1   
for a in range(0,26):
    if (count_one[a] != count_two[a]):
        answer += abs(count_one[a]-count_two[a])
print(answer)

