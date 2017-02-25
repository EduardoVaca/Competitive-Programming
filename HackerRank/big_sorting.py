import functools

def comparator(x, y):
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1
    else:
        for i in range(len(x)):
            if x[i] < y[i]:
                return -1
            elif x[i] > y[i]:
                return 1
        return 0

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)
sorted_list = sorted(unsorted, key=functools.cmp_to_key(comparator))

for n in sorted_list:
    print(n)
