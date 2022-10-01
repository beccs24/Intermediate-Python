# Lab00, CS 9, Rebecca Chang

def areElementsInList(list1, list2):
    ''' This function takes two lists as its parameters (list1 and
        list2). Return True if each element in list1 exists in list2.
        Return False otherwise. If list1 contains no elements, True is
        returned.
    '''
    if len(list1) == 0:
        return True
    else:
        for i in range(len(list1)):
            if list1[i] not in list2:
                return False
        return True

assert areElementsInList(["one",2], [0,"one",2,"three"]) == True
assert areElementsInList([],[1,2,3,4]) == True
assert areElementsInList([1,2,3],[1,2]) == False
assert areElementsInList([1,2,3],[3,2,1]) == True


def alternateCase(s):
    ''' This function takes a string parameter (s) and returns a new
        string that flips the case of each alpha character in s.
        NOTE: Your solution **SHOULD NOT** use Python strings' swapcase()
        method (think of how you can perform this by iterating through
        each character in the string s). Hint, think of utilizing Python
        strings' isupper() and islower() methods.
    '''

    new_s = ""
    for i in range(len(s)):
        if s[i].islower() == True:
            new_s += s[i].upper()
        else:
            new_s += s[i].lower()
    return new_s

assert alternateCase("") == ""
assert alternateCase("This is a Sentence") == "tHIS IS A sENTENCE"
assert alternateCase("CS9") == "cs9"
assert alternateCase("9.95") == "9.95"


def getCharacterCount(s):
    ''' This function takes a string parameter (s) and returns a dictionary
        type where each key in the dictionary is a unique upper-case character
        in s and its associated value is the number of occurences the unique
        character exists in s. Note that the unique characters should be case
        insensitive ("a" and "A" are considered the same and should be stored as
        "A" in the dictionary). Non alpha characters (including whitespaces)
        and their occurences should also be stored in the dictionary.
    '''
    
    dict = {}

    for i in range(len(s)):
        count = 0
        dict[s[i].upper()] = count
        for j in range(len(s)):
            if s[j] == s[i].upper() or s[j] == s[i].lower():
                count+= 1
        dict[s[i].upper()] = count

    return dict
    
x = getCharacterCount("This is a Sentence")
assert x.get("S") == 3
assert x.get("P") == None
assert x.get("I") == 2
assert x.get(" ") == 3

y = getCharacterCount("Pi is Approximately 3.14159")
assert y.get("1") == 2
assert y.get("A") == 2
assert y.get("P") == 3
assert y.get(".") == 1
assert y.get(4) == None

