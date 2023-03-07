'''
Write a function called cumsum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
'''

def cansum(num_list):
    new_list = []
    previous_num = 0
    for num in num_list:
        new_num = num + previous_num
        new_list.append(new_num)
        previous_num = new_num
    return new_list

t = [1, 2, 3]
print(cansum(t))