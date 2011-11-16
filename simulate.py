from math import pi, sin
from numpy import array, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Given in problem
Tn = 1.0         # Natural period
T = 1.1          # Excitation period
a = 0.01         # Pivot excitation amplitude

# Calculated based on irrefutable fact
wn = 2*pi/Tn     # Natural frequency
w = 2*pi/T       # Excitation frequency

# Assumed because we live on Earth
g = 9.81         # Gravitational constant

# Assumed because we believe Newton's law is a differential equation and that
# when it is linearized about the downward equilibrium configuration it is a
# good approximation of the motion for small angles.
l = g/(wn**2)    # Pendulum length

# Nonlinear differential equation of motion in first order form
def f(x, t):
  return array([x[1], -g/l*sin(x[0]) + a/l*w*w*sin(w*t)])

# Initial angle and angular rate
#ic = [0., 0.]
ic = [0., 1.1]

# Numerically integrate the equations
t = linspace(0, 30, 1000)
x = odeint(f, ic, t)

# Plot the response
fig = plt.figure()
host = fig.add_subplot(111)
par1 = host.twinx()

p1, = host.plot(t, x[:,0], 'b-', label=r'$\theta$')
p2, = par1.plot(t, x[:,1], 'g-', label=r'$\dot{\theta}$')
host.set_ylim(min(x[:,0]), max(x[:,0]))
par1.set_ylim(min(x[:,1]), max(x[:,1]))

host.set_xlabel('time, seconds')
host.set_ylabel(r'$\theta$, rad')
par1.set_ylabel(r'$\dot{\theta}$, rad / second')

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

host.tick_params(axis='y', colors=p1.get_color())
par1.tick_params(axis='y', colors=p2.get_color())

plt.title(r'Pendulum response, initial conditions: [{0}, {1}]'.format(x[0,0], x[0,1]))
plt.savefig('pendulum_response_{0}_{1}.png'.format(x[0,0], x[0,1]))
plt.show()
