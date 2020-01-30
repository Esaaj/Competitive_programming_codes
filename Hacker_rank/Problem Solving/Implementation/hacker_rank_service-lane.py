length , test_case = input().split(" ")
input_str = list(input().split(" "))
test_case = int(test_case)
while(test_case):
    start , end = input().split(" ")
    print(min(input_str[int(start):int(end)+1]))
    test_case -= 1