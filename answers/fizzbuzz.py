input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

count = inputs[0]
num1 = inputs[1]
num2 = inputs[2]

for i in range(count):
    if ((i+1)%num1 == 0 and (i+1)%num2 == 0):
        print("FizzBuzz")
    elif ((i+1)%num1 == 0):
        print("Fizz")
    elif ((i+1)%num2 == 0):
        print("Buzz")
    else:
        print((i+1))
