'''
Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
'''

def has_duplicates(t):
    if len(t) != len(set(t)):
        return True
    else:
        return False

t1 = [1, 5, 5, 3, 7]
t2 = [1, 5, 3, 7]
print(has_duplicates(t1))
print(has_duplicates(t2))