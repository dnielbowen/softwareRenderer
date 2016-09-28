import util
import math
import re

import numpy as np

import transforms
import parseObj

imWidth = 600
imHeight = 600
nFrames = 360
nRevolutions = 1
objFilename = "models/wt_teapot.obj"

vertices, faces = parseObj.readObjFile(objFilename)
for iRevolution in range(nFrames):
    th = iRevolution * (2*math.pi/nFrames) * nRevolutions

    matWorld = np.eye(4)
    matWorld[0:2,0:2] = np.mat(
            ((math.cos(th), -math.sin(th)), (math.sin(th), math.cos(th))))

    tr = transforms.TriangleRenderer(imWidth, imHeight)
    for iFace, face in enumerate(faces):
        triangle = [vertices[i-1] for i in face]
        tr.renderTriangle(triangle, matWorld)

    tr.rasterizer.save("frames/frame_%03d.png" % iRevolution)
    print("Saving frame %d" % iRevolution)
