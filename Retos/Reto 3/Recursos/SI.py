
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
plt.style.use("bmh")

#funciion para resolver las ecuaciones diferenciales
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

#funcion par pintar
def plot(S, I, R, t, divide_by=1):
    # Dibujamos los datos de S(t), I(t) y R(t)
    fig, ax = plt.subplots()
    ax.plot(t, S / divide_by, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.plot(t, I / divide_by, 'r', alpha=0.5, lw=2, label='Infectado')
    ax.plot(t, R / divide_by, 'g', alpha=0.5, lw=2, label='Recuperado con inmunidad')
    ax.set_xlabel('Tiempo /días')
    ax.set_ylabel(f'Número (dividido por {divide_by:,})')
    legend = ax.legend()
    fig.show() # descomenta esto si no estás en Jupyter

# población inicial, N.
N = 7_813_000# poblaciçon de un país como España
 
# Número inicial de infectados y recuperados, I0 and R0.
I0 = 422
R0 = 0
 
# El resto, casi todo N, es susceptible de infectarse
S0 = N - I0 - R0
 
# Tasas de contagio y recuperación.
beta = 5.4 # contagio
gamma = 0.0 # recuperación
 
# Pasos temporales (en días)
t = np.linspace(0, 30, 30)
 
# condiciones iniciales
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T
 
plot(S, I, R, t) # Datos sin normalizar
plot(S, I, R, t, divide_by=N) # Datos normalizados


# import numpy as np

# def rungekutta2_fgw(f,g,w,t0,x0,y0,z0,h,muestras):
#     tamano = muestras +1
#     tabla = np.zeros(shape=(tamano,4),dtype=float)
#     tabla[0] = [t0,x0,y0,z0]
#     ti = t0
#     xi = x0
#     yi = y0
#     zi = z0
#     for i in range(1,tamano,1):
#         K1x = h * f(ti,xi,yi,zi)
#         K1y = h * g(ti,xi,yi,zi)
#         K1z = h * w(ti,xi,yi,zi)
        
#         K2x = h * f(ti+h, xi + K1x, yi+K1y, zi +K1z)
#         K2y = h * g(ti+h, xi + K1x, yi+K1y, zi +K1z)
#         K2z = h * w(ti+h, xi + K1x, yi+K1y, zi +K1z)

#         xi = xi + (1/2)*(K1x+K2x)
#         yi = yi + (1/2)*(K1y+K2y)
#         zi = zi + (1/2)*(K1z+K2z)
#         ti = ti + h
        
#         tabla[i] = [ti,xi,yi,zi]
#     tabla = np.array(tabla)
#     return(tabla)

# # Programa
# # Parámetros de las ecuaciones

# binfecta = 1.3
# grecupera   = 0
# # Ecuaciones
# f = lambda t,S,I,R : -binfecta*S*I
# g = lambda t,S,I,R : binfecta*S*I - grecupera*I
# w = lambda t,S,I,R : grecupera*I
# # Condiciones iniciales
# t0 = 0
# S0 = 1.0
# I0 = 0.001
# R0 = 0.0

# # parámetros del algoritmo
# h = 1.0
# muestras = 51

# # PROCEDIMIENTO
# tabla = rungekutta2_fgw(f,g,w,t0,S0,I0,R0,h,muestras)
# ti = tabla[:,0]
# Si = tabla[:,1]
# Ii = tabla[:,2]
# Ri = tabla[:,3]
# # SALIDA
# np.set_printoptions(precision=6)
# print(' [ ti, Si, Ii, Ri]')
# print(tabla)

# # Grafica tiempos vs población
# import matplotlib.pyplot as plt
# plt.plot(ti,Si, label='S')
# plt.plot(ti,Ii, label='I')
# plt.plot(ti,Ri, label='R')
# plt.title('Modelo SIR')
# plt.xlabel('t tiempo')
# plt.ylabel('población')
# plt.legend()
# plt.grid()
# plt.show()
