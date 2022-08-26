'''Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that
takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of
a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a; the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt; the fourth column is the absolute value
of the difference between the two estimates.'''

from doctest import testfile
import math

def mysqrt(a):
    """Calculates square root using Newton's method:
    https://en.wikipedia.org/wiki/Newton's_method
    
    a - positive integer < 0;
    x - estimated value, in this case a/2
    """
    x = a / 2 
    epsilon = 0.0000001
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
            break
        x = y


def test_square_root(number_list):
    print("a	mysqrt(a)	math.sqrt(a)	diff")
    print("-	---------	------------	----")
    # for num in number_list:
    #     col1 = float(num)
    #     col2 = mysqrt(num)
    #     col3 = math.sqrt(num)
    #     col4 = abs(mysqrt(num) - math.sqrt(num))

    #     print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)

    for a in number_list:
        print("%.1f	%.5f	        %.5f	        %f" % (a,mysqrt(a), math.sqrt(a), abs(mysqrt(a)-math.sqrt(a))))

test_square_root(range(1,10))

'''
Output
a       mysqrt(a)       math.sqrt(a)    diff
-       ---------       ------------    ----
1.0     1.00000         1.00000         0.000000
2.0     1.41421         1.41421         0.000000
3.0     1.73205         1.73205         0.000000
4.0     2.00000         2.00000         0.000000
5.0     2.23607         2.23607         0.000000
6.0     2.44949         2.44949         0.000000
7.0     2.64575         2.64575         0.000000
8.0     2.82843         2.82843         0.000000
9.0     3.00000         3.00000         0.000000
'''