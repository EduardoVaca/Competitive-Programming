class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hash_table = dict()
        for i in range(len(A)):
            if (B - A[i]) in hash_table:
                return [hash_table[(B - A[i])], i+1]
            elif not A[i] in hash_table:
                hash_table[A[i]] = i+1
        return []
