import sys

change_s = input().strip()
original_s = input().strip()
k = int(input().strip())

if change_s != original_s:
    min_size = min(len(change_s), len(original_s))
    different_index = min_size
    for i in range(min_size):
        if change_s[i] != original_s[i]:
            different_index = i
            break

    if different_index == 0 and k > len(change_s) + len(original_s):
        print('Yes')
        sys.exit()
    k -= (len(change_s) - different_index)
    k -= (len(original_s) - different_index)
    if k < 0:
        print('No')
        sys.exit()

if k % 2 == 0:
    print('Yes')
elif k > len(original_s) * 2:
    print('Yes')
else:
    print('No')
