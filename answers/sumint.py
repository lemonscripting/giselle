base = int(input())
input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

total = 0
for i in range(base):
    total += inputs[i]
print(total)