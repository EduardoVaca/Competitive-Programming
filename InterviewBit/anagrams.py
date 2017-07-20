def get_key(word):
    letters = [0 for _ in range(26)]
    for c in word:
        letters[ord(c)-97] += 1
    key = ''
    for i in range(26):
        key += ''.join([chr(i+97) for _ in range(letters[i])])
    return key

class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        result = []
        index_dict = dict()
        counter = 0
        for i in range(len(A)):
            key = get_key(A[i])
            if key in index_dict:
                result[index_dict[key]].append(i+1)
            else:
                result.append([i+1])
                index_dict[key] = counter
                counter += 1
        return result
