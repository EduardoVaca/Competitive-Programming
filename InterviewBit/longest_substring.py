class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        appeared_letters = [-1 for _ in range(256)]
        max_letters = 0
        current_count = 0
        i = 0
        while i < len(A):
            if appeared_letters[ord(A[i])] == -1:
                appeared_letters[ord(A[i])] = i
                current_count += 1
                i += 1
            else:
                max_letters = max(max_letters, current_count)
                current_count = 0
                i = appeared_letters[ord(A[i])] + 1
                appeared_letters = [-1 for _ in range(256)]
        return max(current_count, max_letters)
