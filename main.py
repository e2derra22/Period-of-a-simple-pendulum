import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
from matplotlib import pyplot as plt

def equations(y0, t):
    theta, x = y0
    f = [x, -(g/l) * sin(theta)]
    return f

def plot_results(time, theta1):
    plt.plot(time, theta1[:,0])
    s = '(Initial Angle = ' + str(initial_angle) + ' degrees)'
    plt.title('Pendulum motion: ' + s)
    plt.xlabel('time(s)')
    plt.ylabel('angle(rad)')
    plt.grid(True)

g = float(input('Enter the gravitational acceleration: '))
l = float(input('Enter the lenght of the pendulum (cm): ')) * 100
initial_angle = float(input('Enter the initial angle: '))

time = np.arange(0, 10.0, 0.025)
theta0 = np.radians(initial_angle)
x0 = np.radians(0.0)
theta1 = odeint(equations, [theta0, x0], time) 

plot_results(time, theta1)

plt.show()