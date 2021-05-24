# INTERPOLACION LINEAL

# Input section
# Primer punto
print('Ingrese el primer punto:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

# Segundo punto
print('Ingrese el segundo punto:')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

# Punto a calcular
xp = float(input('Ingrese el punto a calcular (xp): '))

# Valor del punto
yp = y0 + ((y1-y0)/(x1-x0)) * (xp - x0)

print('EL valor interpolado linealmente en %0.4f es %0.4f' %(xp,yp))