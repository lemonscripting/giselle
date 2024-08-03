base = int(input())
total = []
total.append(base)

def even(a):
    return a // 2 
    
def odd(a):
    return a * 3 + 1
    
def test(a):
    if (a%2 == 0):
        return 0
    else:
        return 1

while (total[- 1] != 1):
    last = total[len(total) - 1]
    a = test(last)
    if (a == 0):
        add = even(last)
    else:
        add = odd(last)
    total.append(add)
        
sentence = ""
for i in range(len(total)):
    sentence += str(total[i]) 
    sentence += " "
print(sentence)