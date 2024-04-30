from numpy import *

def calculate(a : list[complex] , z : complex) -> complex:
    p = complex(0,0)
    q = complex(0,0)
    i = len(a) - 1
    for r in reversed(a):
        p += r
        p *= z
        q *= z
        q += r * i
        i -= 1
        pass
    return z - p / q

def newton_iteration_judge(a : list[complex] , z0 : complex , N : int , epsilon : float) -> int:
    z = complex(0,0)
    z1 = z0
    i = 1
    while i < N:
        if abs(z - z1) < epsilon :
            return i
        z = z1
        z1 = calculate(a , z)
        i += 1
    return N

