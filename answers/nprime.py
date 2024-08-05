import math

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

current_prime_count = 0
r = 0
case = int(input())
while(current_prime_count != case):
    a = is_prime(r)
    if (a == True):
        current_prime_count += 1
        num = r
    r += 1
    
print(r - 1)