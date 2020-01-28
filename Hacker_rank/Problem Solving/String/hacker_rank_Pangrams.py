input_str = input()
input_list = list(input_str.lower())
alphabet = list("abcdefghijklmnopqrstuvwyxz")
count = 0
for a in alphabet :
    if a in input_list:
        count += 1
if(count == 26 ):
    print("pangram")
else:
    print("not pangram")
