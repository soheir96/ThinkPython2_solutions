def check_fermat(a,b,c,n):
	if n > 2 and a**n + b**n == c**n:
		print ("Holy smokes, Fermat is wrong!")
	else:
		print ("Nah.. Fermat is right on this.")

def run_fermat():
    a = int(input("Enter value for integer 1: "))
    b = int(input("Enter value for integer 2: "))
    c = int(input("Enter value for integer 3: "))
    n = int(input("Enter value for exponent: "))
    check_fermat(a,b,c,n)

run_fermat()
