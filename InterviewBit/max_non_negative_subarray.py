
def getMax(A, B):
    if sum(A) > sum(B):
        return A
    elif sum(B) > sum(A):
        return B
    else:
        if len(A) > len(B):
            return A
        elif len(B) > len(A):
            return B
        else:
            return A

def maxset(A):
    biggest_set = []
    start = -1
    current = 0
    while current < len(A):
        if A[current] > -1 and start == -1:
            start = current
        elif A[current] < 0:
            if start > -1:
                biggest_set = getMax(biggest_set, A[start:current])
                start = -1
        current += 1
    
    if start > -1:
        # Last sub array wasn´t considered
        biggest_set = getMax(biggest_set, A[start:])
    return biggest_set