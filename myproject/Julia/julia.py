from numpy import *

def fill_julia_set_judge(N : int , c : complex , z0 : complex , omega : float = 2) -> int :
    R = max(abs(c) , 2)
    z = z0
    i = 1
    while i < N :
        z = pow(z , omega) + c
        if abs(z) > R:
            return i
        i+=1
    
    return N

