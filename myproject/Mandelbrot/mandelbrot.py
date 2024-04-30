from numpy import *

def mandelbrot_set_judge(N : int , c : complex) -> int :
    R = max(abs(c) , 2)
    z = complex(0,0)
    i = 1
    while i < N :
        z = z * z + c
        if abs(z) > R:
            return i
        i+=1
    
    return N

