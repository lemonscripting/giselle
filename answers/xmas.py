gcount = int(input())

arr = [0] * gcount

for i in range(gcount):
    a = int(input())
    arr[a-1] = i + 1

for item in arr:
    print(item)