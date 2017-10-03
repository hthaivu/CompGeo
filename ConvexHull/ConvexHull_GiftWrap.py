# Solving Convex Hull problem using Gift Wrapping (Jarvis March) algorithm
# The algorithm works as follow:
#  1. Finding the first right most point
#  2. Finding the next point that is farthest to the right (smallest angle) using cross product
#  3. Iterate until come back to the initial point

import numpy as np
import matplotlib.pyplot as plt
import time

#----------------algorithm--------------------------------


def cross(origin, p1, p2):
    # Calculate cross product of vectors origin-p1 and origin-p2
    # To check the relative position of points p1, p2 with regards to the origin point
    cross = ((p2[0] - origin[0]) * (p1[1] - origin[1]) - (p1[0] - origin[0]) * (p2[1] - origin[1]))
    return cross


def giftwrap(points):
    # Input: an array of points in 2-D
    # Output: list of points on the Convex Hull

    # Number of point must be more than 3
    if len(points) < 3:
        return print("Number of points must be greater than 3")

    hull = []
    # Start with the right most point and add to the convex hull
    start = points[0]
    for pt in points[1:]:
        if pt[0] > start[0]:
            start = pt
    hull.append(start)
    current = start
    nexthull = None

    # Start the iteration
    # .all() is logical function for numpy array type
    while (nexthull != start).any():

        # choose initial point for nexthull iteration, must be different than current point
        if (current == points[0]).all():
            nexthull = points[1]
        else:
            nexthull = points[0]

        # iterate to get the right-most (smallest angle) point (nexthull) in respect to the current point
        for checkpoint in points:

            # make sure the checkpoint is a different point
            if (checkpoint == current).all() or (checkpoint == nexthull).all():
                continue

            # positive cross product implies that the checkpoint is to the left of the nexthull, and thus update the nexthull to be the checkpoint
            else:
                direction = cross(current, nexthull, checkpoint)
                if direction > 0:
                    nexthull = checkpoint

        # add the qualified nexthull to the hull and move on
        hull.append(nexthull)
        current = nexthull

    return np.array(hull)


#--------------main---------------------------------------

# Implementation
n = 1000

tic = time.clock()
points = np.random.rand(n, 2)
hull = giftwrap(points)
toc = time.clock()

h = len(hull)
# Summary
print("Gift Wrapping Algorithm on ", n, "points")
print("Convex Hull of size:", h)
print("Elapsed time:", toc - tic)


# Plot the points and convex hull
plt.plot(points[:, 0], points[:, 1], 'o')
plt.plot(hull[:, 0], hull[:, 1], 'r-')
plt.show()
