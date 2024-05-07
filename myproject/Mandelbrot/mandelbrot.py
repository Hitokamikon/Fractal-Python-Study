from numpy import *

def mandelbrot_set_judge(N : int , c : complex , omega : float = 2) -> int :
    R = max(abs(c) , 2)
    z = complex(0,0)
    i = 1
    while i < N :
        z = pow(z , omega) + c
        if abs(z) > R:
            return i
        i+=1
    
    return N

