
def romanToInt(A):
    roman_keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = roman_keys[A[0]]
    for i in range(1, len(A)):
        if roman_keys[A[i]] > roman_keys[A[i-1]]:            
            number += (roman_keys[A[i]] - 2 * roman_keys[A[i-1]])
        else:
            number += roman_keys[A[i]]
    return number


n = input()
print(romanToInt(n))