"""
The following functions are all INTENDED to check whether a string contains any
lowercase letters, but at least some of them are wrong. For each function,
describe what the function actually does (assuming that the parameter is a string).
"""

def any_lowercase1(s):
    # function returns True if first letter of string is lower case, otherwise returns False 
    for c in s:
        if c.islower():
            return True
        else:
            return False

# print(any_lowercase1('Hello'))

def any_lowercase2(s):
    # function doesn't check input string
    # function always returns true as the string argument in the if statement is wrapped in string quotes 
    # 'c' is lowercase, so will always be true 
    # should be c.islower() not 'c'.islower()
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# print(any_lowercase2('Hello'))

def any_lowercase3(s):
    # function returns True if last letter of string is lower case, otherwise returns False 
    for c in s:
        flag = c.islower()
    return flag

# print(any_lowercase3('HellO'))

def any_lowercase4(s):
    # if any character is lowercase, func will return true 
    # flag starts as false, but if a lowercase is found, it will stay True for rest of iterations
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# print(any_lowercase4('HellO'))

def any_lowercase5(s):
    # if any letter in string is uppercase, will return False 
    # c = 'P' --> not c.islower() = 'True' --> if statement will return False 
    for c in s:
        if not c.islower():
            return False
    return True

# print(any_lowercase5('heLlo'))