import math
import random
import collections
import numpy as np

# This should really be shared between rasterizer and geometry transformer
Vertex = collections.namedtuple('Vertex', 'pos color')

# I need to go from local to world to view to perspective to normalized to 
# screen

randomColor = lambda: tuple(random.randint(0,255) for i in range(3))
point = lambda x,y,z: np.mat(((x), (y), (z), (1))).transpose() # Homog coords
cubeVertices = [
    Vertex(point( 1, 1, 1), randomColor()),
    Vertex(point(-1, 1, 1), randomColor()),
    Vertex(point(-1,-1, 1), randomColor()),
    Vertex(point( 1,-1, 1), randomColor()),
    Vertex(point( 1, 1,-1), randomColor()),
    Vertex(point(-1, 1,-1), randomColor()),
    Vertex(point(-1,-1,-1), randomColor()),
    Vertex(point( 1,-1,-1), randomColor()),
]

cubeFaceIndices = [
    (0,1,3), (1,2,3), # Top face
    (4,5,6), (4,6,7), # Bottom face
    (1,0,4), (1,4,5), # Front-right
    (2,3,4), (3,7,4), # Front-left
    (1,6,2), (1,5,6), # Back-right
    (3,7,6), (2,3,6), # Back-left
]

################################################## WORLD
# Place the object in the world --- keep it at home for now
matWorld = np.eye(4)

################################################## VIEW
cameraPos = np.array((45,45,45))
cameraTarget = np.array((0,0,0))
cameraUp = np.array((0,1,0))
cameraZ = cameraTarget - cameraPos
cameraZ = cameraZ / np.linalg.norm(cameraZ)
cameraY = np.cross(np.cross(cameraZ, cameraUp), cameraZ)
cameraY = cameraY / np.linalg.norm(cameraY)
cameraX = np.cross(cameraZ, cameraY)

# I'm sure there's a more efficient/direct way of writing matView other than 
# computing its inverse, but this is the most non-blackbox method
matView = np.eye(4)
matView[0:3, 0:4] = np.mat((cameraX, cameraY, cameraZ, cameraPos)).transpose()
matView = np.linalg.inv(matView)

################################################## PROJECTION
projWinWidth = 2
aspectRatio = 1 # 4/3, etc
projWinHeight = projWinWidth/aspectRatio
projHFOV = 63 # Degrees
d = projWinWidth/(2*math.tan(projHFOV/2*math.pi/180))
farPlane = 1000

matProj = np.mat((
    (2*d/projWinWidth, 0, 0, 0),
    (0, 2*d/projWinHeight, 0, 0),
    (0, 0, (farPlane+d)/(farPlane-d), 2*d*farPlane/(farPlane-d)),
    (0, 0, 1, 0)))

################################################## SCREEN
imWidth = 600
imHeight = 600

matWindow = np.eye(4)
matWindow[0:2, 0:2] = np.mat(((imWidth/2, 0), (0, -imHeight/2)))
matWindow[0:2, 3] = np.mat(((imWidth/2), (imHeight/2)))

# Everything is now in NDC (after perspective divide) --- I now need to compute 
# the screen transformation

################################################## COMPOSITES
matWV = matWorld.dot(matView)
matWVP = matWV.dot(matProj)
matWVPS = matWVP.dot(matWindow)

##################################################
# Alright, let's start transforming geometry!

v1w = cubeVertices[2].pos
v1v = matView * v1w
v1p = (matProj * v1v) / v1v[2]
v1s = matWindow * v1p

def vertexProcessor(v):
    vw = v.pos # Vertex in local/world space (same in this case)
    vv = matView * vw # Vertex in view space
    vp = (matProj * vv) / vv[2] # Projection and perspective divide
    vs = matWindow * vp # Window scaling
    return Vertex(pos=vs, color=v.color)

primitive = []
for v in (cubeVertices[i] for i in cubeFaceIndices[3]):
    primitive.append(vertexProcessor(v))

Rasterizer
