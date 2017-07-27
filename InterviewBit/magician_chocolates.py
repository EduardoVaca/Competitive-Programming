import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        heap_neg_B = [-x for x in B]
        heapq.heapify(heap_neg_B)
        total_candies = 0
        modulo = 1000000007
        for _ in range(A):
            current_max = -(heapq.heappop(heap_neg_B))        
            total_candies += current_max
            heapq.heappush(heap_neg_B, -(int(current_max/2)))        
        return total_candies % modulo
