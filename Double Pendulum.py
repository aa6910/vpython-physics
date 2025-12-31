import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.81
L1 = 1
L2 = 1
m1 = 1
m2 = 1

def double_pendulum(t, z):
    theta1, theta2, w1, w2 = z
    dw1dt = (-g*(2*m1 + m2)*np.sin(theta1) - (m2)*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*(m2)*(L2*(w2)**2+ L1*np.cos(theta1 - theta2)*L1*(w1)**2))/(L1*(2*m1 + m2 - (m2)*np.cos(2*theta1 - 2*theta2)))
    dw2dt = (2*np.sin(theta1 - theta2)*((L1)*(m1+m2)*w1**2)+g*(m1+m2)*np.cos(theta1) +(L2)*(m2)*np.cos(theta1-theta2)*(w2)**2)/((L2)*(2*m1 + m2 + (m2)*np.cos(2*theta1 - 2*theta2)))
    return [w1, w2, dw1dt, dw2dt]

T = [0, 100]
initial = [1, 1, 0, 0]
sol = solve_ivp(double_pendulum, T, initial, t_eval=np.linspace(0, 100, 1000))
theta1 = sol.y[0]
theta2 = sol.y[1]
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)
plt.plot(sol.t, x1, label = '$\tx_{1}$')
plt.plot(sol.t, x2, label = '$\tx_{2}$')
plt.legend()
plt.show()
