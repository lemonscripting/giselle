cases = int(input())
arr = [0] * cases

input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

for i in range(cases):
    a = inputs[i]
    arr[i] = a ** (1/3)
    
for item in arr:
    print(int(round(item)))

