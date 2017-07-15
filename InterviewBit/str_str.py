
def has_substring(candidate, word):
    if len(word) > len(candidate):
        return False
    for i in range(len(word)):
        if word[i] != candidate[i]:
            return False
    return True

def strStr(haystack, needle):
    if needle and haystack:
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and has_substring(haystack[i:], needle):
                return i
    return -1