input_string = input()
split_values = input_string.split()
inputs = [int(value) for value in split_values]

maxp = inputs[0]
actions = inputs[1]
current = 0
for i in range(actions):
    a = input()
    if (a == "LAND"):
        current += 1
    elif (a == "EVACUATE"):
        current = 0
    else:
        current -= 1
    if (current > maxp):
        print("PLAN REJECTED")
        quit()
print("PLAN ACCEPTED")