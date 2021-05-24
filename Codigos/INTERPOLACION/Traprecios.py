from math import* 

def trapecios(f, a, b, m):
    h=(b-a)/m
    s=0
    for i in range (1, m):
        s= s+f(a+1*h)
    r=h/2*(f(a)+2*s+f(b))
    return r

def f(x): return log(x)
r=trapecios(f, 1, 2, 100)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 200)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 300)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 400)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 500)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 600)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 700)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 800)
print(r)

def f(x): return log(x)
r=trapecios(f, 1, 2, 900)
print(r)