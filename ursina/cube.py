#! /usr/bin/env python

from ursina import *

app = Ursina()
cube = Entity(model='cube', color=hsv(100, 50, 20), scale=2, collider='box')

def spin():
    cube.animate('rotation_y', cube.rotation_y+360, duration=2, curve=curve.in_out_expo)

cube.on_click = spin
EditorCamera()
app.run()