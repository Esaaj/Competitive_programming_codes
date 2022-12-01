testCase = int(input())

for _ in range(0, testCase):
    arr = input().split(" ")
    print(arr)
    D, L, R = int(arr[0]), int(arr[1]), int(arr[2])
    if(D>L and D<R):
        print("Take second dose now")
    elif(D<L):
        print("Too Early")
    elif(D>R):
        print("Too Late")