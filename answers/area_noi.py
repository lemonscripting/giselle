cases = int(input())
highest = 0
for i in range(cases):
    
    input_string = input()
    split_values = input_string.split()
    inputs = [int(value) for value in split_values]
    sum = inputs[0] * inputs[1]
    if (sum > highest):
        highest = sum
print(highest)
