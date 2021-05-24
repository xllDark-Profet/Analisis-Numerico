from sympy import*
def newton(f, v, u, e, m):
    df=diff(f,v)
    for i in range(m):
        r=u-float(f.subs(v,u))/float(df.subs(v,u))
        if abs(r-u)<e:
            return [r,i]
        u=r
    return [None]

x=Symbol('x')
f=exp(x)-pi*x
[r,i]= newton(f,x,1.5,0.000001,10)
print(r)
print(i)