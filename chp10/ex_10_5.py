'''
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
'''

def is_sorted(t):
    new_t = sorted(t)
    if t == new_t:
        return True
    else:
        return False
    
print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
