# If any of the three lengths is greater than the sum of the other two, then you cannot
# form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a “degenerate” triangle.)

def is_triangle(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_b + side_c > side_a and side_a + side_c > side_b:
        print("Yes")    
    else:
        print("No")

def check_triangle():
    a = int(input("Enter value for side 1: "))
    b = int(input("Enter value for side 2: "))
    c = int(input("Enter value for side 3: "))
    is_triangle(a,b,c)

check_triangle()