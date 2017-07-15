
def common_prefix(s1, s2):
    smaller = s1 if len(s1) < len(s2) else s2
    for i in range(len(smaller)):
        if s1[i] != s2[i]:
            return s1[:i]
    return smaller

def longestCommonPrefix(A):
    current_prefix = A[0]
    for word in A[1:]:
        if word.find(current_prefix) != 0:
            current_prefix = common_prefix(current_prefix, word)
    return current_prefix