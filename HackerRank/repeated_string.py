s = input().strip()
n = int(input().strip())
a_dict = {0: 0}
a_word = 0
a_count = 0
key = 1

for c in s:
    if c == 'a':
        a_word += 1
    a_dict[key] = a_word
    key += 1

a_count = int(n / len(s)) * a_word
a_count += a_dict[n % len(s)]

print(a_count)
