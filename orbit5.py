import vpython
from vpython import *
import numpy as np
import math



import vpython
from vpython import *
import numpy as np
import math

gc = gcurve(color=color.green)
gv = gcurve(color=color.blue)
gb = gcurve(color=color.cyan)


def force(planet1,planet2,m1,m2):
    rvec = planet2.pos - planet1.pos
    rmag = mag(rvec)
    rhat = (rvec)*(1/rmag)
    forcemag = m1*m2/(rmag**2)
    forcevec = -forcemag*rhat
    return forcevec
    
    

star = sphere(radius = 5, color=color.yellow,pos=vector(0,0,0))

planet1 = sphere(radius = 1, color=color.green,pos=vector(0,30,0), make_trail=True, trail_radius=0.5, interval=10, retain = 10000000000)
planet2 = sphere(radius = 1, color=color.cyan,pos=vector(0,35,0), make_trail=True, trail_radius=0.5, interval=10, retain = 10000000000)


def verlet(planet,planet2,star,m,m2):
    q = -1
    t = 0
    dt = 0.002
    r = planet.pos
    r2 = planet2.pos
    v_mag = (1000/mag(r))**0.5
    v2_mag = (1000/mag(r2))**0.5
    v = vector(v_mag, 0, 0) 
    v2 = vector(v2_mag,0, 0) 

    while q == -1:
        rate(20000)
        a = (1/m) * force(star, planet, 1000, m) + (1/m) * force(planet, planet2, m, m2)
        a2 = (1/m2) * force(star, planet2, 1000, m2) + (1/m2) * force(planet2, planet, m2, m)
        r = r + v * dt + 0.5 * a * (dt**2)
        r2 = r2 + v2 * dt + 0.5 * a2 * (dt**2)
        planet.pos = r
        planet2.pos = r2
        a_new = (1/m) * force(star, planet, 1000, m) + (1/m) * force(planet, planet2, m, m2)
        a2_new = (1/m2) * force(star, planet2, 1000, m2) + (1/m2) * force(planet2, planet, m2, m)
        v = v + 0.5 * (a + a_new) * dt
        v2 = v2 + 0.5 * (a2 + a2_new) * dt
        t += dt
        gc.plot(mag(r), t)  
        gv.plot(mag(r2), t)

verlet(planet1,planet2,star,1,3)
