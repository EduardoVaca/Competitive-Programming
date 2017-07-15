
def get_words(s):
    words = []
    start = -1
    for i in range(len(s)):
        if s[i] != ' ' and start == -1:
            start = i
        elif s[i] == ' ' and start != -1:
            words.append(s[start:i])
            start = -1
    if start != -1:
        words.append(s[start:])
    return words

def reverseWords(A):
    words = get_words(A)
    return ' '.join(list(reversed(words)))

print(reverseWords('hi there you'))