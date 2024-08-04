input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

import math
print(math.gcd(inputs[0],inputs[1]))
