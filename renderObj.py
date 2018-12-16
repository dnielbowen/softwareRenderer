import util
import math
import re

import numpy as np

import transforms
import parseObj
import parseSTL

imWidth = 600
imHeight = 600
nFrames = 1
nRevolutions = 1
modelFilename = "models/cube.stl"

# vertices, faces = parseObj.readObjFile(modelFilename)
vertices, faces = parseSTL.parseSTL(modelFilename)
for iRevolution in range(nFrames):
    th = iRevolution * (2*math.pi/nFrames) * nRevolutions

    matWorld = np.eye(4)
    matWorld[0:2,0:2] = np.mat(
            ((math.cos(th), -math.sin(th)), (math.sin(th), math.cos(th))))

    tr = transforms.TriangleRenderer(imWidth, imHeight)
    tr.changeCamera(np.array((3 + iRevolution*10/nFrames,3,3)))
    for iFace, face in enumerate(faces):
        triangle = [vertices[i-1] for i in face]
        tr.renderTriangle(triangle, matWorld, useWireframe=True)

    tr.rasterizer.save("frames/frame_%03d.png" % iRevolution)
    print("Saving frame %d" % iRevolution)
