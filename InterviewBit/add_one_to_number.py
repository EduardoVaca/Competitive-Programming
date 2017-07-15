def look_for_index(A):
    for i, e in reversed(list(enumerate(A))):
        if e < 9:
            return i
    return -1

def valid_list(A):
    for i in range(len(A)):
        if A[i] != 0:
            return A[i:]
    return []

def plusOne(A):
    index = look_for_index(A)
    if index < 0:
        return [1] + [0 for _ in range(len(A))]
    else:
        A[index] += 1
        A = A[:index + 1] + [0 for _ in range(len(A) - index - 1)]
        return valid_list(A)

