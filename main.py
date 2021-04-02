import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
from matplotlib import pyplot as plt
import math

result_list = []

def period(l, g, initial_angle):
    return 2 * math.pi * math.sqrt(l/g) * math.sin(initial_angle)

g = float(input('Enter the gravitational acceleration: '))
L = float(input('Enter the lenght of the pendulum (cm): ')) / 100
initial_angle = float(input('Enter the initial angle: '))

for i in range(4):
    result_list.append(period(L, g, initial_angle))

    if L > 0.2: 
        L -= 0.1

temp = [50, 40, 30, 20]
plt.scatter(result_list, temp)
plt.plot(result_list, temp, label='Actual')
plt.plot(np.unique(result_list), np.poly1d(np.polyfit(result_list, temp, 1))(np.unique(result_list)), color='red', label='Best fit')
s = '(Initial Angle = ' + str(initial_angle) + ' degrees)'
plt.title('Pendulum motion: ' + s)
plt.xlabel('Period of one oscillation (s)')
plt.ylabel('lenght (cm)')
plt.legend()
plt.grid(True)

gradient = np.polyfit(result_list, temp, 1)

print(result_list)
print(f'Gradient = {gradient}')

for i in result_list:
    print(i * 20)
plt.show()

