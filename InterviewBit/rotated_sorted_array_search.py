
def find_pivot(A, start, end):
    mid = int((start+end)/2)
    if A[mid] >= A[start] and A[mid] <= A[end]:
        return -1
    if A[mid] >= A[start] and A[mid] >= A[end]:
        if mid == 0 or (A[mid] > A[mid-1] and A[mid] > A[mid+1]):
            return mid+1
    if A[mid] < A[start]:
        return find_pivot(A, start, mid)
    else:
        return find_pivot(A, mid, end)

def bs(A, start, end, element):
    if start > end:
        return -1
    mid = int((start+end)/2)
    if A[mid] == element:
        return mid
    elif A[mid] < element:
        return bs(A, mid+1, end, element)
    else:
        return bs(A, start, mid-1, element)

def search(A, B):
    pivot = find_pivot(A, 0, len(A) - 1)
    if pivot >= 0:
        left_list = A[:pivot]
        right_list = A[pivot:]
        left_result = bs(left_list, 0, len(left_list)-1, B)
        right_result = bs(right_list, 0, len(right_list)-1, B)
        right_result = right_result + len(left_list) if right_result > -1 else right_result
        return max(right_result, left_result)
    else:
        return bs(A, 0, len(A)-1, B)
