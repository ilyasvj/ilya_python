import numpy as np
import turtle as t
import math
import random

class Plotter:
    def __init__(self, width, height):
        self.wn = t.Screen()
        self.wn.width = width
        self.wn.height = height
        self.wn.title('Plotter')
        self.wn.bgcolor("White")
        self.wn.setup(width=width, height=height)
        self.wn.tracer(0)

    def plot(self, x, y):
        min_x = x[0]
        max_x = x[0]
        for kx in x:
            if kx > max_x:
                max_x = kx
            if kx < min_x:
                min_x = kx
        min_y = y[0]
        max_y = [0]
        for ky in y:
            if ky > max_y:
                max_y = ky
            if ky < min_y:
                min_y = ky

        tmp = t.Turtle()
        tmp.penup()
        tmp.goto(-self.wn.width/2, 0)
        tmp.pendown()

        for i in range(len(x)):
            loc_x = (x[i] - min_x)/(max_x - min_x)*self.wn.width - self.wn.width/2
            loc_y = (y[i] - min_y)/(max_y - min_y)*self.wn.height - self.wn.height/2
            tmp.goto(loc_x, loc_y)
        tmp.penup()

class Water:
    def __init__(self, fd = 10000, fs = 2000, ti = 0.2, Tc = 1):
        self.fd = fd
        self.fs = fs
        self.ti = ti
        self.Tc = Tc

    def get_signals(self, r, phi):
        time = list()
        time.append(float(0))
        while time[-1] < self.Tc:
            time.append(time[-1]+1/self.fd)
        print('time')
        delay = r/1500
        signal = list()
        for i in range(len(time)):
            signal.append(random.random()-0.5)
            if time[i] > delay and time[i] < delay + self.ti:
                signal[-1] += math.sin(2*math.pi*self.fs*time[i])
            return( (time, signal) )

water = Water()
(time, signal) = water.get_signals(1000, 0)

plotter = Plotter(400,400)