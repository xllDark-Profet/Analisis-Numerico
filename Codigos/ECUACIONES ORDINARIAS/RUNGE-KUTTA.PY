from pylab import*

from pylab import*

def rungekutta(f,x,y,h,m):
    u=[]
    v=[]
    for i in range(m):
        k1=h*f(x,y)
        k2=h*f(x+h/2,y+k1/2)
        k3=h*f(x+h/2,y+k2/2)
        k4=h*f(x+h,y+k3)
        y=y+1/6*(k1+2*k2+2*k3+k4)
        x=x+h
        u=u+[x]
        v=v+[y]
    return [u,v]


def f(x,y):return 0.4*x-0.018*x*y
[u,v]=rungekutta(f,30,4,1,20)
plot(u,v,'or')
def y(x):return exp(x)+x**2+x
x=arange(0,2.1,0.1)
plot(x,y(x),'ob')
grid(True)
show()