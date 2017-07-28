class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        result = []
        if B > len(A):
            return result
        start = end = 0
        current_numbers = {}    
        while end < len(A):        
            if A[end] in current_numbers:            
                current_numbers[A[end]] += 1
            else:
                current_numbers[A[end]] = 1
            if end-start == B-1:
                result.append(len(current_numbers))
                current_numbers[A[start]] -= 1
                if current_numbers[A[start]] == 0:
                    current_numbers.pop(A[start])
                start += 1            
            end += 1        
        return result
