'''
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
'''

def chop(t):
    ''' Removes the first and last item from list t and returns None'''
    for i in [0,-1]:
        del t[i]
    
t = [1, 2, 3, 4]
chop(t)
print(t)