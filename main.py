import random, time, turtle as tr
from molecule import Molecule, System


amount_of_molecules = 50
x_range = 150
y_range = 150
min_radius = 4
max_radius = 8
min_speed = 10
max_speed = 70

box_size = 500


molecules = [Molecule(
    x=round(random.uniform(-1, 1)*x_range),
    y=round(random.uniform(-1, 1)*y_range),
    radius=round(min_radius + random.random() * (max_radius - min_radius)),
    color='black',
    speed=round(min_radius + random.random() * (max_radius - min_radius))
) for _ in range(amount_of_molecules)]

System(molecules, box_size / 2)


tr.tracer(1000)
System.brownian_motion()
tr.done()
