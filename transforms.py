import math
import collections

import numpy as np

import util
import rasterizer

# Vertices go from local to object to camera to projection to screen.

# Combines rasterizer and camera parameters (FOV)
class TriangleRenderer:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.rasterizer = rasterizer.Rasterizer(self.w, self.h)

        self.changeCamera(np.array((2, 1, 1)))

    # pos is np.array((-,-,-))
    def changeCamera(self, cameraPos, cameraTarget=np.array((0,0,0)), hfov=60):
        cameraUp = np.array((0,1,0))
        cameraZ = cameraTarget - cameraPos
        cameraZ = cameraZ / np.linalg.norm(cameraZ)
        cameraY = np.cross(np.cross(cameraZ, cameraUp), cameraZ)
        cameraY = cameraY / np.linalg.norm(cameraY)
        cameraX = np.cross(cameraZ, cameraY)

        matView = np.eye(4)
        matView[0:3, 0:4] = np.mat((
            cameraX, cameraY, cameraZ, cameraPos)).transpose()
        matView = np.linalg.inv(matView)
        self.matView = matView

        ################################################## PROJECTION
        projWinWidth = 2
        aspectRatio = 1 # 4/3, etc
        projWinHeight = projWinWidth/aspectRatio
        d = projWinWidth/(2*math.tan(hfov/2*math.pi/180))
        farPlane = 1000

        matProj = np.mat((
            (2*d/projWinWidth, 0, 0, 0),
            (0, 2*d/projWinHeight, 0, 0),
            (0, 0, (farPlane+d)/(farPlane-d), 2*d*farPlane/(farPlane-d)),
            (0, 0, 1, 0)))
        self.matProj = matProj

        matWindow = np.eye(4)
        matWindow[0:2, 0:2] = np.mat(((self.w/2, 0), (0, -self.h/2)))
        matWindow[0:2, 3] = np.mat(((self.w/2), (self.h/2)))
        self.matWindow = matWindow

    def vertexProcessor(self, v, matWorld):
        vl = util.vert2mat(v)
        vw = matWorld * vl
        vv = self.matView * vw # Vertex in view space
        vp = (self.matProj * vv) / vv[2] # Projection and perspective divide
        vs = self.matWindow * vp # Window scaling
        return util.Vertex(
                float(vs[0]), float(vs[1]), float(vs[2]), color=v.color)

    def renderTriangle(self, vertices, matWorld, useWireframe=True):
        vsScreen = [self.vertexProcessor(v, matWorld) for v in vertices]
        if useWireframe:
            self.rasterizer.rasterizeTriangleWireframe(vsScreen)
        else:
            self.rasterizer.rasterizeTriangleScanline(vsScreen)
