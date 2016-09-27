import util
import d

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

imFilename = "triangleRasterized.png"
