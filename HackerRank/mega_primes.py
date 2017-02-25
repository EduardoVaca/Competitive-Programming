def is_prime(n): 
    if n == 1:
        return False   
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    a = 5
    b = 2

    while a * a <= n:
        if n % a == 0:
            return False
        a += b
        w = 6 - b
    return True

first, last = [int(x) for x in input().strip().split(' ')]
mega_primes = 0
just_primes = True
for i in range(first, last + 1):
    just_primes = True
    for digit in reversed(str(i)):
        if not is_prime(int(digit)):
            just_primes = False
            break
    if just_primes and is_prime(i):        
        mega_primes += 1
print(mega_primes)
