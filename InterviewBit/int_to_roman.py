class Solution:
    
    def incremented_roman(self, roman):
        result = ''
        for letter in roman:
            if letter == 'I':
                result += 'X'
            elif letter == 'V':
                result += 'L'
            elif letter == 'X':
                result += 'C'
            elif letter == 'L':
                result += 'D'
            elif letter == 'C':
                result += 'M'
        return result
        
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        num_1_9 = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
        roman = ''
        num = str(A)
        for i in range(len(num)):
            if i > 0:
                roman = self.incremented_roman(roman)
            if num[i] != '0':
                roman += num_1_9[num[i]]
        return roman
