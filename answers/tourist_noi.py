input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

days = inputs[0]
single = inputs[1]
unlimited = inputs[2]

input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

total_val = 0
for i in range(len(inputs)):
    a = inputs[i]*single
    if (a >= unlimited):
        total_val += unlimited
    else:
        total_val += a
print(total_val)
    