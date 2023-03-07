'''
Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''

def nested_sum(nested_lists):
    total = 0
    for nl in nested_lists:
        total += sum(nl)
    return total 

t = [[1, 2], [3], [4, 5, 6]]
print("Total value of all numbers in the nested list {} = {}".format(t,nested_sum(t)))
