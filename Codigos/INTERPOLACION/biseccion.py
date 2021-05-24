from math import*
def biseccion(f, a, b, e):
    while b-a>=e:
        c=(a+b)/2
        if f(c)==0:
            return c
        else:
            if f(a)*f(c)>0:
                a=c
            else:
                b=c
    return c

def f(x): return pi
c=biseccion(f, 0, 2, 0.0001)
print(c)