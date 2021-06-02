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
R0 = 20
 
# El resto, casi todo N, es susceptible de infectarse
S0 = N - I0 - R0
 
# Tasas de contagio y recuperación.
beta = 5.4 # contagio
gamma = 0.047 # recuperación
 
# Pasos temporales (en días)
t = np.linspace(0, 30, 30)
 
# condiciones iniciales
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T
 
plot(S, I, R, t) # Datos sin normalizar
plot(S, I, R, t, divide_by=N) # Datos normalizados