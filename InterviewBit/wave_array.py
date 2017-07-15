class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        wave_list = []
        i = 0
        while i < len(A):
            if i + 1 < len(A):
                wave_list.append(A[i + 1])
            wave_list.append(A[i])
            i += 2
        return wave_list