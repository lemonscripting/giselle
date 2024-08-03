input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

if (inputs[0] == 1):
    print("Hello World")
else:
    input_string1 = input()
    split_values1 = input_string1.split()
    inputs1 = [int(value) for value in split_values1]
    print(inputs1[0]*inputs1[1])