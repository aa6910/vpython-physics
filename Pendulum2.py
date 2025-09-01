import vpython
from vpython import *
import numpy as np
import math


gc = gcurve(color=color.red)
gv = gcurve(color=color.blue)
gb = gcurve(color=color.cyan)

L = 1
t=0
dt = 0.01
q = -1
theta = np.pi/4
w = 0
c= 0.5
A= 0.5
g = 9.81
f = 2

def acc(t):
    return -9.81*np.sin(t)

bob = sphere(radius = 0.3, color=color.yellow*0.5,pos=vector(0,-1,0))
hang = box(size=vector(1,1,1),pos=vector(0,0.5,0))
rod = cylinder(radius=0.01,pos=vector(0,0,0),axis=vector(0,-1,0),length=-bob.pos.y)

#myarrow = attach_arrow( bob, 'pos' , scale=-2.0)

while q == -1:
    rate(200)
    a = acc(theta) -c*w + A*sin(f*dt)
    theta1 = theta + w*dt + 0.5*a*(dt**2)
    a1 = acc(theta1) -c*w + A*sin(f*dt)
    w = w + 0.5*(a+a1)*dt
    bob.pos.x = sin(theta)
    bob.pos.y = -cos(theta)
    rod.axis.x= sin(theta)
    rod.axis.y = -cos(theta)
    t += dt
    gc.plot(theta, w)
    #gv.plot(dt, bob.pos.y)
    #gb.plot(dt, theta)
    theta = theta1
    
