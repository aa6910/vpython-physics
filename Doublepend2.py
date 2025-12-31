#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 18:21:13 2025

@author: deck
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vpython import *
import sympy

g = 9.81
L1 = 1
L2 = 1
m1 = 1
m2 = 1
t = 0
dt = 0.01

theta1 = np.pi/4
theta2 = np.pi/3
w1 = 0
w2 = 0

bob_1 = gcurve(color = color.red)
bob_2 = gcurve(color = color.blue)

def acc1(theta1, theta2, w1, w2):
    #return (-g*(2*m1 + m2)*np.sin(theta1) - (m2)*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*(m2)*(L2*(w2)**2+ L1*np.cos(theta1 - theta2)*L1*(w1)**2))/(L1*(2*m1 + m2 - (m2)*np.cos(2*theta1 - 2*theta2))+1e-10)
    num1 = -g*(2*m1 + m2)*np.sin(theta1)
    num2 = -m2*g*np.sin(theta1 - 2*theta2)
    num3 = -2*np.sin(theta1 - theta2)*m2*(w2**2*L2 + w1**2*L1*np.cos(theta1 - theta2))
    den = L1*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    alpha1 = (num1 + num2 + num3) / den
    return alpha1
def acc2(theta1, theta2, w1, w2):
    #return (2*np.sin(theta1 - theta2)*((L1)*(m1+m2)*w1**2)+g*(m1+m2)*np.cos(theta1) +(L2)*(m2)*np.cos(theta1-theta2)*(w2)**2)/((L2)*(2*m1 + m2 + (m2)*np.cos(2*theta1 - 2*theta2))+1e-10)
    num1 = 2*np.sin(theta1 - theta2)
    num2 = (w1**2*L1*(m1+m2))
    num3 = g*(m1+m2)*np.cos(theta1)
    num4 = w2**2*L2*m2*np.cos(theta1 - theta2)
    den = L2*(2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    alpha2 = (num1*(num2 + num3 + num4)) / den
    return alpha2
    
while True:
    rate(500)
    theta1_new = theta1 + w1*dt + 0.5*acc1(theta1, theta2, w1, w2)*dt**2   
    theta2_new = theta2 + w2*dt + 0.5*acc2(theta1, theta2, w1, w2)*dt**2 
    w1_new = w1 + 0.5*dt*(acc1(theta1_new, theta2_new, w1, w2) + acc1(theta1, theta2, w1, w2))
    w2_new = w2 + 0.5*dt*(acc2(theta1_new, theta2_new, w1, w2) + acc2(theta1, theta2, w1, w2))
    theta1 = theta1_new
    theta2 = theta2_new
    t += dt
    bob_1.plot(t,w1)
    bob_2.plot(t,w2)
