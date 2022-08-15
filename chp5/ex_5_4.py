'''
n must be greater than 0 (n>0) since n need to approach 0
'''

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
recurse(-1, 0) # RecursionError: maximum recursion depth exceeded in comparison