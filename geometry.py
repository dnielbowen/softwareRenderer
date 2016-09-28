import util

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

################################################## WORLD
# Place the object in the world --- keep it at home for now
matWorld = np.eye(4)

################################################## SCREEN
imWidth = 600
imHeight = 600
imFilename = "cubeRender.png"

for iFace, face in enumerate(cubeFaceIndices):
    triangle = [cubeVertices[i] for i in face]
    tr = transforms.TriangleRenderer(imWidth, imHeight)
    tr.renderTriangle(triangle, matWorld)
    print("Rendered face %d" % iFace)

tr.rasterizer.save(imFilename)
