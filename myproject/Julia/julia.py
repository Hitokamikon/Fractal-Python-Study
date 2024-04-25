from numpy import *

def fill_julia_set_judge(N : int , c : complex , z0 : complex) -> int :
    R = max(abs(c) , 2)
    z = z0
    i = 1
    while i < N :
        z = z * z + c
        if abs(z) > R:
            return i
        i+=1
    
    return N

