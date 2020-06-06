import turtle as tr
import math as mth
import random, time


class Molecule:
    def __init__(self, x, y, radius, color='black', speed=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.direction = round(random.uniform(-180, 180))

    def show(self):
        tr.penup()
        tr.goto(self.x, self.y - self.radius)
        tr.pendown()
        tr.fillcolor(self.color)
        tr.begin_fill()
        tr.circle(self.radius)
        tr.end_fill()

    def hide(self, bg_color='white', pencolor='black'):
        color = self.color
        self.color = bg_color
        tr.pencolor(bg_color)
        self.show()
        tr.pencolor(pencolor)
        self.color = color

    def move(self, length):
        dx = mth.cos(self.direction) * length
        dy = mth.sin(self.direction) * length
        self.x += dx
        self.y += dy


class System:
    molecules = []
    size = 100

    def __init__(self, molecules, size):
        System.molecules = molecules
        System.size = size

    @classmethod
    def show_borders(cls):
        tr.penup()
        tr.goto(0, -cls.size)
        tr.pendown()
        tr.fd(cls.size)
        tr.lt(90)
        tr.fd(2 * cls.size)
        tr.lt(90)
        tr.fd(2 * cls.size)
        tr.lt(90)
        tr.fd(2 * cls.size)
        tr.lt(90)
        tr.fd(cls.size)
        tr.penup()
        tr.goto(0, 0)

    @classmethod
    def show(cls):
        cls.show_borders()
        for x in cls.molecules:
            x.show()

    @classmethod
    def collisions(cls, i):
        x1 = cls.molecules[i].x
        y1 = cls.molecules[i].y
        r1 = cls.molecules[i].radius
        speed = cls.molecules[i].speed
        dy = mth.sin(cls.molecules[i].direction) * speed
        if y1 + dy > cls.size - r1:
            angle = -90 - round((90 -cls.molecules[i].direction)/ (y1 + dy - cls.size + r1) * 10)
            cls.molecules[i].direction = angle if angle <= 180 else angle - 360
        if y1 + dy < -cls.size + r1:
            angle = 90 - round((-90 -cls.molecules[i].direction) / (y1 + dy + cls.size - r1) * 10)
            cls.molecules[i].direction = angle if angle <= 180 else angle - 360
        dx = mth.cos(cls.molecules[i].direction) * speed
        if x1 + dx > cls.size - r1:
            angle = 180 - round(cls.molecules[i].direction / (x1 + dx - cls.size + r1) * 10)
            cls.molecules[i].direction = angle if angle <= 180 else angle - 360
        if x1 + dx < -cls.size + r1:
            angle = round((180 - cls.molecules[i].direction) / (x1 + dx + cls.size - r1) * 10)
            cls.molecules[i].direction = angle if angle <= 180 else angle - 360

        for j in range(len(cls.molecules)):
            if i != j:
                x2 = cls.molecules[j].x
                y2 = cls.molecules[j].y
                r2 = cls.molecules[j].radius
                if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 < r1 + r2:
                    cls.molecules[i].direction, cls.molecules[j].direction = cls.molecules[j].direction, cls.molecules[i].direction
        print(i, cls.molecules[i].direction)

    @classmethod
    def brownian_motion(cls):
        System.show()
        while True:
            for i in range(len(cls.molecules)):
                cls.molecules[i].hide()
                System.collisions(i)
                cls.molecules[i].move(cls.molecules[i].speed)
                cls.molecules[i].show()
