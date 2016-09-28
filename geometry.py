import util
import math

import numpy as np

import transforms

cubeVertices = [
    util.Vertex( 1, 1, 1, util.randomColor()),
    util.Vertex(-1, 1, 1, util.randomColor()),
    util.Vertex(-1,-1, 1, util.randomColor()),
    util.Vertex( 1,-1, 1, util.randomColor()),
    util.Vertex( 1, 1,-1, util.randomColor()),
    util.Vertex(-1, 1,-1, util.randomColor()),
    util.Vertex(-1,-1,-1, util.randomColor()),
    util.Vertex( 1,-1,-1, util.randomColor()),
]

cubeFaceIndices = [
    (0,1,3), (1,2,3), # Top face
    (4,5,6), (4,6,7), # Bottom face
    (1,0,4), (1,4,5), # Front-right
    (2,3,4), (3,7,4), # Front-left
    (1,6,2), (1,5,6), # Back-right
    (3,7,6), (2,3,6), # Back-left
]

imWidth = 800
imHeight = 800
nFrames = 360
nRevolutions = 1

for iRevolution in range(nFrames):
    th = iRevolution * (2*math.pi/nFrames) * nRevolutions

    matWorld = np.eye(4)
    matWorld[0:2,0:2] = np.mat(
            ((math.cos(th), -math.sin(th)), (math.sin(th), math.cos(th))))

    tr = transforms.TriangleRenderer(imWidth, imHeight)
    for iFace, face in enumerate(cubeFaceIndices):
        triangle = [cubeVertices[i] for i in face]
        tr.renderTriangle(triangle, matWorld)

    tr.rasterizer.save("frames/frame_%03d.png" % iRevolution)
    print("Saving frame %d" % iRevolution)
