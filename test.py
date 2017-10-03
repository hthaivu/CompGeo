# from sympy.geometry import *
# P1 = Point(0, 0)
# P2 = Point(3, 4)
# P3 = Point(2, -1)
# test = Point.is_collinear(P1, P2, P3)
# print(P1 is P1)

import numpy as np
points = np.array([[0.10000516, 0.38840325],
                   [0.36184244, 0.21750341],
                   [0.3764111, 0.77043693],
                   [0.06437577, 0.69745481],
                   [0.84811414, 0.14578412],
                   [0.02274081, 0.96101041]])
# print(points)


def cross(origin, p1, p2):
    # Calculate cross product of vectors origin-p1 and origin-p2
    # To check the relative position of points p1, p2 with regards to the origin point
    cross = ((p2[0] - origin[0]) * (p1[1] - origin[1]) - (p1[0] - origin[0]) * (p2[1] - origin[1]))
    return cross


hull = []
# Choose the right most point
start = points[0]
for pt in points[1:]:
    if pt[0] > start[0]:
        start = pt
print("Start:", start)

hull.append(start)
current = start
nexthull = None

print("Hull", hull)

if (current == points[0]).all():
    nexthull = points[0]
else:
    nexthull = points[1]


for checkpoint in points:
    # make sure the checkpoint is a different point
    print("a")
    if (checkpoint == current).all() or (checkpoint == nexthull).all():
        continue
    else:
        direction = cross(current, nexthull, checkpoint)
        if direction > 0:
            nexthull = checkpoint

hull.append(nexthull)
current = nexthull
print("Hull", hull)

if (current == points[0]).all():
    nexthull = points[0]
else:
    nexthull = points[1]


for checkpoint in points:
    # make sure the checkpoint is a different point
    print("a")
    if (checkpoint == current).all() or (checkpoint == nexthull).all():
        continue
    else:
        direction = cross(current, nexthull, checkpoint)
        if direction > 0:
            nexthull = checkpoint

hull.append(nexthull)
current = nexthull
print("Hull", hull)
