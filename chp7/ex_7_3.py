import math 

def estimate_pi():
    """Computes an estimate of pi.
    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """    
    total = 0 
    k = 0 
    constant = 2 * math.sqrt(2) / 9801
    
    while True:
        num = math.factorial(4*k) * (1103 + 26390*k)
        den = math.factorial(k)**4 * 396**(4*k)

        total += num / den
        term = constant * num/den 

        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / (constant * total)
    
print(estimate_pi())
