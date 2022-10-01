def integerDivision(n, k):
    '''
    The parameters n and k are positive integers (you may assume n is >= 0 and k is > 0).
    This function recursively returns the quotient (n // k) without explicitly using
    the // operator or a pre-defined function.
    '''
    
    if n < k:
        return 0
    if n == k:
        return 1
    return integerDivision(n-k, k) + 1


def collectEvenInts(listOfInt):
    '''
    The parameter listOfInt is a list containing positive integer values.
    This function will return a list containing only even values in listOfInt
    in the order that they appear in listOfInt. If there are no even values in listOfInt,
    then this function should return an empty list.
    '''

    if len(listOfInt) == 0:
        return []
    if listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])  
    
    
def countVowels(someString):
    '''
    This function will take a string value (someString) and return the number of
    vowels (‘A’,’E’,’I’,’O’,’U’,’a’,’e’,’i’,’o’,’u’) that exists in someString.
    '''
    
    vowelList = ['A','E','I','O','U','a','e','i','o','u']
    if len(someString) == 0:
        return 0
    if someString[0] in vowelList:
        return 1 + countVowels(someString[1:])
    else:
        return countVowels(someString[1:])


def reverseString(s):
    '''
    The parameter s is a string. This function will return a string in the reverse order of s.
    Note that the reverse of an empty string is an empty string.
    '''

    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    return s[-1] + reverseString(s[:-1])
    

def removeSubString(s, sub):
    '''
    The parameters s and sub are strings that contain at least one character.
    This function will return a string where all occurrences of sub are removed in the order
    it appears in the string s. Your solution SHOULD NOT use the string’s replace method.
    '''

    if len(s) < len(sub):
        return s
    if s == sub:
        return ""
    if sub in s[:len(sub)]:
        print(s[len(sub):])
        return removeSubString(s[len(sub):], sub)
    else:
        print(s[1:len(sub)+1])
        return s[0] + removeSubString(s[1:], sub)
