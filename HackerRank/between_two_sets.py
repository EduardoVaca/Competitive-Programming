
def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def are_factors(l, n):
    for e in l:
        if n % e != 0:
            return False
    return True

def is_factor(l, n):
    for e in l:
        if e % n != 0:
            return False
    return True

set_one_size, set_two_size = input().strip().split(' ')
set_one_size, set_two_size = [int(set_one_size), int(set_two_size)]
set_one = input().strip().split(' ')
set_two = input().strip().split(' ')
s_1 = []
s_2 = []
min_value = 101

for i in range(set_one_size):
    s_1.append(int(set_one[i]))

for i in range(set_two_size):
    s_2.append(int(set_two[i]))
    if s_2[i] < min_value:
        min_value = s_2[i]
del s_2[s_2.index(min_value)]

factors = get_factors(min_value)
count = 0

for factor in factors:
    if are_factors(s_1, factor) and is_factor(s_2, factor):
        count += 1

print(count)
