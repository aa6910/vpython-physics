import vpython
from vpython import *
import numpy as np
import math

scene.background = color.cyan
box(pos=vector(0,-1,0),size=vector(200,0.5,200),color=color.green)

def adjustAngle():
    angleSliderReadout.text = angleSlider.value + " degrees"
scene.append_to_caption("\n\n")
angleSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustAngle)

scene.append_to_caption(" Angle = ")
angleSliderReadout = wtext(text=angleSlider.value)


def adjustSpeed():
    speedSliderReadout.text = speedSlider.value + " m/s"
scene.append_to_caption("\n\n")
speedSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustSpeed)

scene.append_to_caption(" Speed = ")
speedSliderReadout = wtext(text=speedSlider.value)


def adjustHeight():
    heightSliderReadout.text = heightSlider.value + " m"
scene.append_to_caption("\n\n")
heightSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustHeight)

scene.append_to_caption(" Height = ")
heightSliderReadout = wtext(text=heightSlider.value)


def adjustMass():
    massSliderReadout.text = massSlider.value + " kg"
scene.append_to_caption("\n\n")
massSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustMass)

scene.append_to_caption(" Mass = ")
massSliderReadout = wtext(text=massSlider.value)


def adjustRadius():
    radiusSliderReadout.text = radiusSlider.value + " m"
scene.append_to_caption("\n\n")
radiusSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustRadius)

scene.append_to_caption(" Radius = ")
radiusSliderReadout = wtext(text=radiusSlider.value)


def adjustDragCoeffiecient():
    dragCoeffiecientSliderReadout.text = dragCoeffiecientSlider.value
scene.append_to_caption("\n\n")
dragCoeffiecientSlider = slider(left=10, min=0, max=90, step=1,
                     bind=adjustDragCoeffiecient)

scene.append_to_caption(" Drag Coeffiecient = ")
dragCoeffiecientSliderReadout = wtext(text=dragCoeffiecientSlider.value)


def launch():

    u = speedSlider.value
    theta = math.radians(angleSlider.value)
    h = heightSlider.value
    m = massSlider.value
    r = radiusSlider.value
    d = dragCoeffiecientSlider.value

    pi = 3.141592653589793
    A = (pi)*(r**2)
    p = 1.28
    gd = 9.81
    dt = 0.01
    k = (0.5*d*p*A)/m

    xd = -50
    yd = h
    vxd = u*cos(angleSlider.value)
    vyd = u*sin(angleSlider.value)
    print("Launching the projectile!")
    ball = sphere(pos = vector(0,yd,0),radius = r,color = color.blue)
    while yd > 0:
        rate(50)
        vd = sqrt((vxd**2)+(vyd**2))
        axd = -(vxd/vd)*k*(vd**2)
        ayd = -gd -(vyd/vd)*k*(vd**2)
        vxd = vxd + axd*dt
        vyd = vyd + ayd*dt
        xd = xd + vxd*dt + 0.5*axd*(dt)**2
        yd = yd + vyd*dt + 0.5*ayd*(dt)**2
        ball.pos.x = xd
        ball.pos.y = yd

button(text="Launch!", bind=launch)


