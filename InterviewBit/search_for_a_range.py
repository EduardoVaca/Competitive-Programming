def find_start(start, end, A, val):
    if start > end:
        return -1
    mid = int(start+end)/2
    if A[mid] == val:
        if mid == 0 or A[mid-1] != val:
            return mid
        else:
            return find_start(start, mid-1, A, val)
    elif A[mid] < val:
        return find_start(mid+1, end, A, val)
    else:
        return find_start(start, mid-1, A, val)
        
def find_end(start, end, A, val):
    if start > end:
        return -1
    mid = int(start+end)/2
    if A[mid] == val:
        if mid == len(A)-1 or A[mid+1] != val:
            return mid
        else:
            return find_end(mid+1, end, A, val)
    elif A[mid] < val:
        return find_end(mid+1, end, A, val)
    else:
        return find_end(start, mid-1, A, val)

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        left = find_start(0, len(A)-1, A, B)
        right = find_end(0, len(A)-1, A, B)
        return [left, right]
