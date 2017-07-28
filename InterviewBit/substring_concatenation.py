def get_dict(B):
    dictionary = {}
    for item in B:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary

def is_substring(words, index, dictionary, size):
    while index < len(words):
        if words[index:index+size] in dictionary:
            dictionary[words[index:index+size]] -= 1
            if dictionary[words[index:index+size]] == 0:
                dictionary.pop(words[index:index+size])
                if not dictionary:
                    return True
        else:
            break
        index += size
    return False

class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        result = []
        if not B:
            return result
        size = len(B[0])    
        original_dict = get_dict(B)
        start = 0
        for i in range(len(A)):
            current_dict = dict(original_dict)       
            if is_substring(A, i, current_dict, size):
                result.append(i)
        
        return result
