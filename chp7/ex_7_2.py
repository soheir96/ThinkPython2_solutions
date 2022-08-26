'''The built-in function eval takes a string and evaluates it using the Python interpreter.
For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated.'''

import math 

def eval_loop():
    while True:
        user_expression = input('> Enter expression to be evaluated: ')
        if user_expression == 'done':
            print('Exiting program')
            break
        print(eval(user_expression))

eval_loop()