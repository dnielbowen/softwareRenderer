import collections
import random
import numpy as np

# Vertex = collections.namedtuple('Vertex', 'pos color')
Vertex = collections.namedtuple('Vertex', 'x y z color')
Point3 = collections.namedtuple('Point3', 'x y z')
Point4 = collections.namedtuple('Point3', 'x y z w')

randomColor = lambda: tuple(random.randint(0,255) for i in range(3))
point = lambda x,y,z: np.mat(((x), (y), (z), (1))).transpose()
vert2mat = lambda v: np.mat(((v.x), (v.y), (v.z), (1))).transpose()
