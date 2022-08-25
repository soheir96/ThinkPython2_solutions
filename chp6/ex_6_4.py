'''A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.'''

def is_power(a, b):
    # condition 1 - is a divisible by b? 
    if a % b != 0:
        return False 
    
    # condition 2 - base case a = b
    if a == b:
        return True
    
    # condition 3 - a/b is a power of b 
    if is_power(a / b, b):
        return True
    else:
        return False

print(is_power(8,2))
print(is_power(9,2))